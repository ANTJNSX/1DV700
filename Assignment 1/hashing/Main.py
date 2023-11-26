import os
import HashSet as hset
import matplotlib.pyplot as plt

# path to file
path1 = os.getcwd() + '/Assignment 1/hashing/words1.txt'
path2 = os.getcwd() + '/Assignment 1/hashing/words2.txt'
path3 = os.getcwd() + '/Assignment 1/hashing/words1_shift.txt'

wordsHash = hset.HashSet()   # Create new empty HashSet
# wordsHash.init()             # Initialize with eight empty buckets

# Fill hashmap
with open(path3, "r", encoding="utf-8") as file:
    for line in file:
        word = str(line)
        wordsHash.add(line)

# print(wordsHash.as_list(), 2*'\n')

print("Bucket list size =", wordsHash.bucket_list_size())
print("Max bucket size =", wordsHash.max_bucket_size())
print("Zero bucket ration =", round(wordsHash.zero_bucket_ratio(), 2))


# Example on the different hashdumps with small changes to input
# print('\n')
# print(wordsHash.get_hash("aaa"))
# print(wordsHash.get_hash("aab"))
# print(wordsHash.get_hash("aac"))
# print(wordsHash.get_hash("aad"))

# Hashing solution 1 results
    # 231
    # Bucket list size = 256
    # Max bucket size = 7
    # Zero bucket ration = 0.12

# Hashing solution 2 results improved hash function
    # 203
    # Bucket list size = 256
    # Max bucket size = 7
    # Zero bucket ration = 0.09

# Hashing solution 3 results improvement to sporadic behaviour

    # 152
    # Bucket list size = 256
    # Max bucket size = 10
    # Zero bucket ration = 0.1

# STATISTICAL TESTS

# Bar graph
fig, ax = plt.subplots()

# Plotting zero bucket ratio on a logarithmic scale
ax.bar("Zero Bucket Ratio", wordsHash.zero_bucket_ratio(), color='blue')
ax.set_yscale('log')  # Set y-axis to logarithmic scale

# Plotting max buckets
ax.bar("Max Buckets", wordsHash.max_bucket_size(), color='orange')

# Plotting bucket size
ax.bar("Bucket List Size", wordsHash.bucket_list_size(), color='green')

# Adding labels and title
ax.set_ylabel('Values')
ax.set_title('Hash Set Metrics Overview')

# Show the plot
plt.show()
