import json
from time import sleep
import requests
from bs4 import BeautifulSoup, Tag
import os

ALREADY_PARSED_FILE = "bin/tmp/gems_already_parsed.txt"
OUTPUT_FILE = "bin/output/gem_xp.json"

results = {}


def setup_files():
    os.makedirs("bin/output", exist_ok=True)
    os.makedirs("bin/tmp", exist_ok=True)
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "x") as f:
            json.dump({}, f)
    if not os.path.exists(ALREADY_PARSED_FILE):
        with open(ALREADY_PARSED_FILE, "x"):
            pass
    with open(OUTPUT_FILE, "r") as f:
        results.update(json.load(f))


def create_gem_list():
    url = "https://poegems.com/json"
    response = requests.get(url)
    data = response.json()
    all_gems = {gem["name"] for gem in data}

    already_parsed = None
    with open(ALREADY_PARSED_FILE, "r") as f:
        already_parsed = set(f.read().split("\n"))

    gems_to_parse = all_gems - already_parsed
    return gems_to_parse


class TooManyRequests(Exception):
    pass


def scrape_gem_xp(gem_name):
    url = f"https://www.poewiki.net/wiki/{gem_name.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 429:
        print("Too many requests")
        raise TooManyRequests
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find(
        "table",
        class_="wikitable responsive-table skill-progression-table",
    )
    if type(table) is not Tag:
        print("table type:", type(table))
        print(f"Could not find table for {gem_name}")
        raise ValueError(f"Could not find table for {gem_name}")
    rows = list(table.find_all("tr"))
    max_xp = 0

    for row in rows:
        cells = row.find_all("td")
        if cells:
            try:
                value = int(cells[-1].text)  # Last cell is total xp value
                if value > max_xp:
                    max_xp = value
            except ValueError:  # Value might be "N/A"
                pass

    results[gem_name] = max_xp


def main():
    setup_files()
    gems_to_parse = create_gem_list()
    for gem in gems_to_parse:
        while True:
            try:
                scrape_gem_xp(gem)
                with open(ALREADY_PARSED_FILE, "a") as f:
                    f.write(gem + "\n")
                with open(OUTPUT_FILE, "w") as f:
                    json.dump(results, f, indent=4, sort_keys=True)
                break
            except requests.RequestException as e:
                print(f"Failed to scrape {gem}: {e}")
                break
            except ValueError as e:
                print(f"Failed to scrape {gem}: {e}")
                break
            except TooManyRequests:
                print("Too many requests, waiting 60 seconds")
                sleep(60)
        sleep(2)


if __name__ == "__main__":
    main()
