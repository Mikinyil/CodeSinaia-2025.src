from functools import reduce
import random
from collections import OrderedDict

# read inputs parameters from the console
count = 100 # int(input("Number of values?> "))
min_value = 12 # int(input("Minimum value?> "))
max_value = 85 # int(input("Maximum value?> "))

# generate count values in the range [min_value, max_value] and store them in a the values map
# randoms_map - associates each random value to the zero-based index/iteration where it was generated
# <key=random_value, value=[index1, index2, index3, ...]> 
randoms_map = {}
for i in range(0, count):
    r = random.randint(min_value, max_value)
    if r not in randoms_map:
        randoms_map[r] = []
    randoms_map[r].append(i)

# write the random values in the order in which they were generated, in the file "dataset.txt"
with open("dataset.txt", "w") as data_file:
    for r in randoms_map.keys():
        data_file.write(f"{r} {randoms_map[r]}\n")

# how many distinct randoms were generated?
print(f"Count of unique randoms: {len(randoms_map.keys())}")

# what's the smallest and the largest random?
sorted_randoms = sorted(randoms_map.keys())
print(f"Min random: {sorted_randoms[0]}; Max random: {sorted_randoms[-1]}")

# what are the topN most frequent numbers?
topN = 10 # int(input("Count of most frequent numbers?> "))
# randoms_array - list of objects, each object containing the "value" and the "count" number of
# times that value was generated
randoms_array = []
for random_value in randoms_map.keys():
    randoms_array.append({"value" : random_value, "count" : len(randoms_map[random_value])}) 
# sort all objects in the array by their count field, in reverse order
randoms_array.sort(key=lambda x: x["count"], reverse=True)

# build a set of custom lines of text, each extracted from each object in the array
lines = map(
    lambda r: f'random {r["value"]} occurred {r["count"]} times',
    randoms_array[:topN]
)
# join all the lines by the new-line character and print the result
print("\n".join(lines))
