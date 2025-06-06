import pandas
from RandomNumber import RandomNumber

# Deserialize the data set in from json file
# Parameters:
#    file_name (string): the name of file containing the json serialization
# Returns:
#   ([RandomNumber]): array of RandomNumber objects
def deserialize_data_set(file_name):
    data_set = []
    with open(file_name, "r") as json_file:
        for json_record in json_file:
            random_number = RandomNumber.from_json(json_record)
            data_set.append(random_number)
    return data_set

################ MAIN SCRIPT ################
data_set = deserialize_data_set("dataset.json")
for random_number in data_set:
    print(random_number)