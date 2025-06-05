import random

count = 100 # count of random values to generate
min_value = 12 # min value that may be generated
max_value = 168 # max value that may be generated
data_set = [] # the data set (array) holding all generated randoms
top_counts = 10 # The top N randoms with the most occurrences

# Generate the dataset
print(f"---- Generate {count} random numbers in the range [{min_value} - {max_value}] in the dataset.txt file.")
with open("dataset.txt", "w") as dataFile:
    for i in range(0, count):
        r = random.randint(min_value, max_value)
        data_set.append(r)
        dataFile.write(f"{r}\n")

# Count the occurrences of each number in the dataset
print(f"---- Build a map linking each random (key) to the number of times it was generated (value).")
map = {} # map of {key:number, value:occurence}
for i in range(len(data_set)):
    # if data_set[i] not in map:
    #     map[data_set[i]] = 1
    # else:
    #     map[data_set[i]] += 1
    try:
        map[data_set[i]] += 1
    except KeyError:
        map[data_set[i]] = 1

# Sort the map by occurrences and print the top N
print(f"---- Print the top {top_counts} randoms with the most number of occurrences, in descending order.")
sorted_data_set = sorted(map.items(), key=lambda x: x[1], reverse=True)
for i in range(top_counts):
    print(f"random {sorted_data_set[i][0]} generated {sorted_data_set[i][1]} times")