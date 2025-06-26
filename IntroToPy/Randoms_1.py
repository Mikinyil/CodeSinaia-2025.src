import random
import statistics

# Read input parameters from the console
count = 1000 # int(input("Number of values?> "))
min_value = 12 # int(input("Minimum value?> "))
max_value = 85 # int(input("Maximum value?> "))
print(f"Generating {count} randoms in the range [{min_value}, {max_value}]")

# Generate count values in the range [min_value, max_value] and store them in a the values map
# randoms_map - associates each random value to the zero-based index/iteration where it was generated
# <key=random_value, value=[index1, index2, index3, ...]> 
randoms_map = {}
for i in range(0, count):
    r = random.randint(min_value, max_value)
    if r not in randoms_map:
        randoms_map[r] = []
    randoms_map[r].append(i)

# Write a text file "dataset.txt" with each random on a line, its value followed by the indexes where it occurred
with open("dataset.txt", "w") as data_file:
    for r in randoms_map.keys():
        data_file.write(f"{r} {randoms_map[r]}\n")

# Print a few statistics: min, max random values,  mean, median(aka average) and standard deviation (aka stdev) of the sequence.
print(f"Count of unique randoms: {len(randoms_map.keys())}")
sorted_randoms = sorted(randoms_map.keys())
print(f"Min random: {sorted_randoms[0]}; Max random: {sorted_randoms[-1]}")
print(f"Mean of the sequence: {statistics.mean(sorted_randoms)}")
print(f"Median of the sequence: {statistics.median(sorted_randoms)}")
print(f"Standard Deviation of the sequence: {statistics.stdev(sorted_randoms)}")

# Read from the input the desired topN count of most frequent randoms that should be printed.
# Then, store in an array all the randoms along with their individual count. Each entry in the array is an object with two fields:
# - value: the random value
# - count: the value's frequency or count of occurrences in the sequence. 
# In the end the array is sorted in the descending order of each object's _count_ value and the first topN are printed out.
topN = 10 # int(input("Count of most frequent numbers?> "))
randoms_array = []
for random_value in randoms_map.keys():
    randoms_array.append({"value" : random_value, "count" : len(randoms_map[random_value])}) 
randoms_array.sort(key=lambda x: x["count"], reverse=True)

# Use a lambda expresion to map the first _topN_ objects from the sorted array to a string showing a random value and the count of its occurrences in the sequence. 
# Join these strings together, each a new line, then print the resulting text.
lines = map(
    lambda r: f'random {r["value"]} occurred {r["count"]} times',
    randoms_array[:topN]
)
print("\n".join(lines))
