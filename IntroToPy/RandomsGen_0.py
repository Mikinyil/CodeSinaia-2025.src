import random

count = 100 # Number of random numbers to generate
nStart = 12 # Start of the range
nEnd = 168 # End of the range
dataSet = [] # List to hold the random numbers data set
nTop = 10 # The top N randoms with the most occurrences

# Generate the dataset
print(f"---- Generating {count} random numbers in the range [{nStart} - {nEnd}] in the dataset.txt file.")
with open("dataset.txt", "w") as dataFile:
    for i in range(0, count):
        r = random.randint(nStart, nEnd)
        dataSet.append(r)
        dataFile.write(f"{r}\n")

# Count the occurrences of each number in the dataset
print(f"---- Build a map linking each random (key) to the number of times it was generated (value).")
map = {} # map of {key:number, value:occurence}
for i in range(len(dataSet)):
    # if dataSet[i] not in map:
    #     map[dataSet[i]] = 1
    # else:
    #     map[dataSet[i]] += 1
    try:
        map[dataSet[i]] += 1
    except KeyError:
        map[dataSet[i]] = 1

# Sort the map by occurrences and print the top N
print(f"---- Print the top {nTop} randoms with the most number of occurrences, in descending order.")
sorted_dataSet = sorted(map.items(), key=lambda x: x[1], reverse=True)
for i in range(nTop):
    print(f"random {sorted_dataSet[i][0]} generated {sorted_dataSet[i][1]} times")