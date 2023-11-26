import os
import HashSet as hset
import matplotlib.pyplot as plt

# path to file
path = os.getcwd() + '/Assignment 1/hashing/words.txt'

wordsHash = hset.HashSet()   # Create new empty HashSet
# wordsHash.init()             # Initialize with eight empty buckets

# Fill hashmap
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        word = str(line)
        wordsHash.add(line)

# print(wordsHash.as_list(), 2*'\n')

print(wordsHash.get_hash("ny"))

print("Bucket list size =", wordsHash.bucket_list_size())
print("Max bucket size =", wordsHash.max_bucket_size())
print("Zero bucket ration =", round(wordsHash.zero_bucket_ratio(), 2))

print('\n')
print(wordsHash.get_hash("aaa"))
print(wordsHash.get_hash("aab"))
print(wordsHash.get_hash("aac"))
print(wordsHash.get_hash("aad"))

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

# Hashing solution 3 results improvement to speratic behaviour

    # 152
    # Bucket list size = 256
    # Max bucket size = 10
    # Zero bucket ration = 0.1

# STATISTICAL TESTS

# x = ("zero bucket ratio", "max buckets", "buckets size")
# y = [wordsHash.zero_bucket_ratio(), wordsHash.max_bucket_size(), wordsHash.bucket_list_size()]

# plt.bar(range(len(x)), y, align='center')
# plt.xticks(range(len(x)), x)
# plt.show()
