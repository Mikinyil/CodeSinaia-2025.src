from RandomNumber import RandomNumber

#  Load the random numbers from give file into a map linking the random to a RandomNumber object.
#  Parameters:
#     file_name (string): The file containing the data set of random numbers.
#  Returns:
#     {random, RandomNumber}: map linking each random to the RandomNumber instance containing it
def load_data_set(file_name):
    map = {}
    with open(file_name, "r") as data_file:
        i = 0
        for rec in data_file:
            r = int(rec)
            if r in map:
                map[r].add_index(i)
            else:
                map[r] = RandomNumber(r, i)
            i += 1
    return map

# Serialize the data set in a json format
# Parameters:
#    data_set ({random, RandomNumber}): map linking each random to the RandomNumber instance containing it
#    file_name (string): the name of file containing the json serialization
def serialize_data_set(data_set, file_name):
    with open(file_name, "w") as json_file:
        for random_number in data_set.values():
            json_file.write(f"{random_number.to_json()}\n")

# Print the top N RandomNums from the data set
# Parameters:
#     top_counts: the count of most frequent randoms to print.
#     map({random, RandomNumber}): map linking each random to the RandomNumber object containing it.
def print_top_occurrences(top_counts, map):
    sorted_random_numbers = sorted(map.values(), reverse=True)
    for i in range(top_counts):
        print(sorted_random_numbers[i])
    
################ MAIN SCRIPT ################
if __name__ == "__main__":
    print(f"---- Load raw data from 'dataset.txt' file.")
    data_set = load_data_set("dataset.txt")

    print(f"---- Save JSON data in the 'dataset.json' file.")
    serialize_data_set(data_set, "dataset.json")

    print(f"---- Print the top 10 randoms with the most number of occurrences, in descending order.")
    print_top_occurrences(10, data_set)
