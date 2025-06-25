import random


count = int(input("Number of values?> "))
min_value = int(input("Minimum value?> "))
max_value = int(input("Maximum value?> "))

# we generate count values in the range [min_value, max_value] and store them in the values array
values = {}
for i in range(0, count):
    r = random.randint(min_value, max_value)
    if r not in values:
        values[r] = []
    values[r].append(i)

# write the numbers in the file "dataset.txt"
with open("dataset.txt", "w") as data_file:
    for r in values.keys():
        data_file.write(f"{r} {values[r]}\n")




