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
if __name__ == "__main__":
    # Deserialize the data_set from the json file (file created by RandomsGen_1.py)
    data_set = deserialize_data_set("dataset.json")
    # Use pandas to extract statistics over the random values and their occurrence counts
    df = pandas.DataFrame({
        "value": [obj.get_value() for obj in data_set],
        "count": [obj.get_count() for obj in data_set],
        "instance" : data_set
    })

    # gather basic statistics: min, max, median, std
    print(f'Values generated: {df["count"].sum()}')
    print(f'Unique values: {len(df)}')
    print(f'Min/Max values: [{df["value"].min()} - {df["value"].max()}]')
    print(f'Median value: {df["value"].median()}')
    print(f'Mean value: {df["value"].mean()}')
    print(f'Standard Deviation: {df["value"].std()}')
