import enum
import json
import os
import signal
import cv2
import numpy as np
from mss import mss
from time import sleep
import pathlib
import pprint
import sys

if len(sys.argv) != 2:
    print("Usage: python bin/img-rec.py <data folder name (e.g. 'orbs')>")
    exit(1)

ITEMS_FOLDER = sys.argv[1]

BASE_PATH = "bin/data/img-rec/"
OUTPUT_PATH = pathlib.Path(BASE_PATH, f"output-{ITEMS_FOLDER}.json")
IMAGE_PATHS = list(pathlib.Path(BASE_PATH, ITEMS_FOLDER).glob("*.png"))
CLICK_PATH = pathlib.Path(BASE_PATH, "clicks", "click.png")
NOCLICK_PATH = pathlib.Path(BASE_PATH, "clicks", "noclick.png")
HOVER_PATH = pathlib.Path(BASE_PATH, "clicks", "hoverclick.png")
PREVIOUS_REGION = pathlib.Path(BASE_PATH, "region.json")

MAIN_MONITOR = 1

CLICK_IMAGE = cv2.imread(CLICK_PATH, cv2.IMREAD_GRAYSCALE)  # type: ignore
NOCLICK_IMAGE = cv2.imread(NOCLICK_PATH, cv2.IMREAD_GRAYSCALE)  # type: ignore
HOVER_IMAGE = cv2.imread(HOVER_PATH, cv2.IMREAD_GRAYSCALE)  # type: ignore


class Clicked(enum.Enum):
    CLICK_DOWN = "down"
    CLICK_UP = "up"
    CLICK_HOVER = "hover"


def path_name(path):
    return path.name.removesuffix(".png")


def load_data(image_paths):
    image_paths = [p for p in image_paths if "click" not in str(p)]
    counts = {path_name(path): 0 for path in image_paths}
    targets = [((cv2.imread(path, cv2.IMREAD_GRAYSCALE)), path_name(path)) for path in image_paths]
    return counts, targets


def capture_screen(region=None):
    with mss() as sct:
        if region is None:
            region = sct.monitors[MAIN_MONITOR]
        screenshot = np.array(sct.grab(region))
        return cv2.cvtColor(screenshot, cv2.COLOR_RGBA2GRAY)


def detect_images(screenshot, target_images, counts):
    matches = []
    for target, path in target_images:
        is_match, similarity = image_match(screenshot, target)
        if is_match:
            matches.append((path, similarity))
    best_match_image, similarity = max(matches, key=lambda x: x[1]) if matches else (None, 0)
    if len(matches) > 1:
        print("WARNING - Matched more than one item:", matches)
        print("Selecting best match:", best_match_image)
    elif len(matches) == 0:
        print("WARNING - No matches found")
    else:
        print("Matched item:", best_match_image, f"{similarity:.4f}")
    if best_match_image:
        counts[best_match_image] += 1
    return matches


def detect_click(screenshot, click_image, noclick_image, hover_image, threshold=0.9):
    _, click_val = image_match(screenshot, click_image, threshold)
    _, noclick_val = image_match(screenshot, noclick_image, threshold)
    _, hover_val = image_match(screenshot, hover_image, threshold)

    o = [
        (click_val, Clicked.CLICK_DOWN),
        (noclick_val, Clicked.CLICK_UP),
        (hover_val, Clicked.CLICK_HOVER),
    ]
    return max(o, key=lambda x: x[0])[1]


def image_match(screenshot, target_image, threshold=0.88):
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val >= threshold, max_val


def select_screen_area():
    with mss() as sct:
        monitor = sct.monitors[MAIN_MONITOR]
        screenshot = np.array(sct.grab(monitor))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2BGR)
        rois = cv2.selectROIs("Select ROI", screenshot, False, False)
        cv2.destroyWindow("Select ROI")
        x, y, w, h = [int(i) for i in rois[0]]
        target = {"left": x, "top": y, "width": w, "height": h}
        x, y, w, h = [int(i) for i in rois[1]]
        click = {"left": x, "top": y, "width": w, "height": h}
        return target, click


def load_regions():
    try:
        with open(PREVIOUS_REGION, "r") as f:
            region, region_click = json.load(f).values()
            print("Loaded previous region, disable by deleting", PREVIOUS_REGION)
            return region, region_click
    except FileNotFoundError:
        for i in range(t := 5):
            print(f"Open Path of Exile window before {t-i} seconds...")
            sleep(1)
        region, region_click = select_screen_area()
        with open(PREVIOUS_REGION, "x") as f:
            json.dump({"region": region, "region_click": region_click}, f)
        return region, region_click


def wait_for_click(click_types: list[Clicked], region):
    while True:
        screenshot = capture_screen(region)
        click = detect_click(screenshot, CLICK_IMAGE, NOCLICK_IMAGE, HOVER_IMAGE)
        if click in click_types:
            break


def save_counts(counts):
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "r") as f:
            data = json.load(f)
        with open(OUTPUT_PATH, "w") as f:
            data = {k: v + data.get(k, 0) for k, v in counts.items()}
            json.dump(data, f, indent=4)
    else:
        with open(OUTPUT_PATH, "x") as f:
            json.dump(counts, f, indent=4)


def main():
    region, region_click = load_regions()
    counts, target_images = load_data(IMAGE_PATHS)

    try:
        while True:
            wait_for_click([Clicked.CLICK_DOWN], region_click)
            sleep(0.05)
            wait_for_click([Clicked.CLICK_UP, Clicked.CLICK_HOVER], region_click)
            sleep(0.1)  # Let poe client update before next screenshot
            screenshot = capture_screen(region)
            detect_images(screenshot, target_images, counts)
            pprint.pprint(sorted(list(counts.items()), key=lambda x: x[1], reverse=True))

    except KeyboardInterrupt:
        # Ignore further interrupts so that saving is not interrupted
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        print("Monitoring stopped.")
        print("Saving data to", OUTPUT_PATH)
        save_counts(counts)
        exit(0)


if __name__ == "__main__":
    main()
