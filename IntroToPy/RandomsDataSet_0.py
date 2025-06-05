import random

from RandomNumber import RandomNumber

#  Generate a dataset of random numbers.
#  Parameters:
#     data_set_file (string): The file containing the data set of random numbers.
#  Returns:
#     {random, RandomNumber}: map linking each random value generated to the RandomNumber instance containing it
def loadDataSet(data_set_file):
    map = {}
    with open(data_set_file, "r") as data_file:
        i = 0
        for rec in data_file:
            r = int(rec)
            if r in map:
                map[r].addIndex(i)
            else:
                map[r] = RandomNumber(r, i)
            i += 1
    return map

# load the data set map and sort the objects in the values set
data_set = loadDataSet("dataset.txt")
sorted_random_numbers = sorted(data_set.values(), reverse=True)
for random_number in sorted_random_numbers:
    print(random_number)

