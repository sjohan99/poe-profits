import json
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Usage: python bin/data/img-rec/plot.py <output-{data}.json>")
    exit(1)

data = sys.argv[1]

with open(f"bin/data/img-rec/{data}", "r") as file:
    data = json.load(file)

items = list(data.keys())
counts = list(data.values())

sorted_items_counts = sorted(zip(counts, items), reverse=True)
sorted_counts, sorted_items = zip(*sorted_items_counts)

total_count = sum(sorted_counts)

plt.figure(figsize=(10, 6))
bars = plt.barh(sorted_items, sorted_counts, color="skyblue")

for bar, count in zip(bars, sorted_counts):
    percentage = (count / total_count) * 100
    plt.text(
        bar.get_width() + 5, bar.get_y() + bar.get_height() / 2, f"{percentage:.2f}%", va="center"
    )

plt.xlabel("Count")
plt.ylabel("Delirium Orbs")
plt.tight_layout()

print("total count:", total_count)
plt.show()
