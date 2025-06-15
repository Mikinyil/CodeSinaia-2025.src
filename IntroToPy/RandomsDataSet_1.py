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

# basic filtering: value with highest count, count of the largest value
maxCountRow = df.loc[df["count"].idxmax()]
print(f'most frequent random: {maxCountRow["value"]} occurred {maxCountRow["count"]} times, at indexes {maxCountRow["instance"].get_indexes()}.')
maxValueRow = df.loc[df["value"].idxmax()]
print(f'largest random {maxValueRow["value"]} generated at indices: {maxValueRow["instance"].get_indexes()}')

# attach a name only to values generated once or twice. Other occurrences are left unnamed
nf = pandas.DataFrame({
    "count" : [1, 2],
    "name": ["unique", "double"]})
# join two data frames by the "count" column
jf = pandas.merge(df, nf, on = "count", how = "outer")
# filter only the unnamed rows
njf = jf[jf["name"].isnan()]
print(f"-------- rows with more than 2 occurrences\n{njf}")
# group all rows by their name, count rows within each group.
gjf = jf.groupby("name")["value"].count()
print(f"-------- count group of occurrences\n{gjf}")