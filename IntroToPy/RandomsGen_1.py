import random

#  Generate a dataset of random numbers.
#  Parameters:
#     count (int): The number of randoms to generate.
#     min_value (int): The smallest value that may be generated.
#     max_value (int): The largest value that may be generated.
#  Returns:
#     [int]: array of random values in the dataset.
def generate_data_set(count, min_value, max_value):
    data_set = []
    for i in range(0, count):
        r = random.randint(min_value, max_value)
        data_set.append(r)
    return data_set

# Save the data set into a file on the disk, one random number per line.
# Parameters:
#   data_set ([int]): the array of randoms.
#   filen_ame (string): the name of the 
def save_data_set(data_set, file_name):
    with open(file_name, "w") as data_file:
        for r in data_set:
            data_file.write(f"{r}\n")

# Count the occurrences of each random.
# Parameters:
#     data_set ([int]): the dataset of random values
# Returns:
#     {random, count}: map linking each random to the number of times it was generated
def build_map(data_set):
    map = {}
    for i in range(len(data_set)):
        # if data_set[i] not in map:
        #     map[data_set[i]] = 1
        # else:
        #     map[data_set[i]] += 1
        try:
            map[data_set[i]] += 1
        except KeyError:
            map[data_set[i]] = 1
    return map

# Print the top N randoms that were generated the most number of times.
# Parameters:
#     top_counts: the count of most frequent randoms to print.
#     map({random, count}): map linking each random to the number of times it occurrs.
def print_top_occurrences(top_counts, map):
    sorted_dataSet = sorted(map.items(), key=lambda x: x[1], reverse=True)
    for i in range(top_counts):
        print(f"random {sorted_dataSet[i][0]} generated {sorted_dataSet[i][1]} times")

################ MAIN SCRIPT ################
print(f"---- Generate 100 random numbers in the range [12 - 168] in the dataset.txt file.")
data_set = generate_data_set(100, 12, 168)

print(f"---- Save the data set in the 'dataset.txt' file.")
save_data_set(data_set, "dataset.txt")

print(f"---- Build a map linking each random (key) to the number of times it was generated (value).")
map = build_map(data_set)

print(f"---- Print the top 10 randoms with the most number of occurrences, in descending order.")
print_top_occurrences(10, map)
