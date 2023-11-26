from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def __init__(self):
        self.size = 0
        self.buckets = [[] for i in range(256)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        # Hashing solution nr 1

        # wordval = 0
        # hashval = 0
        # for char in word:
        #     wordval += ord(char)
        # hashval = wordval % len(self.buckets)
        # return hashval

        # Hashing solution nr 2 optimised

        # prime = 31
        # hash_val = 0

        # for char in word:
        #     hash_val = (hash_val * prime + ord(char)) % 256

        # return hash_val

        # Hashing solution nr 3 optimised for speratic behaviour

        prime = 31
        hash_val = 0

        # for each letter, increase the hash with the prime times
        # the ascii letter and take all of that to the
        # power of the letters index
        for i in range(len(word)):
            hash_val = ((hash_val * prime + ord(word[i])**i)) % 256

        return hash_val

        # Not needed when set bucket size to 256
    # Doubles size of bucket list
    # def rehash(self):
    #     if len(self.buckets) < 256:
    #         new_lst = [[] for _ in range(2 * len(self.buckets))]
    #         for element in self.buckets:
    #             for name in element:
    #                 if name is not None:
    #                     new_lst[self.get_hash(name)].append(name)
    #         self.buckets = new_lst

    #     return self.buckets

    # Adds a word to set if not already added
    def add(self, word):
        if word in self.buckets[self.get_hash(word)]:
            return 0
        else:
            bucket = self.get_hash(word)
            self.buckets[bucket].append(word)
            self.size += 1
            # if len(self.buckets) == self.size:
            #     self.rehash()
        return self.buckets

    # Returns a string representation of the set content
    def to_string(self):
        s = "{ "
        for element in self.buckets:
            for name in element:
                if name is not None:
                    s += name + " "
                else:
                    continue
        s += "}"

        return s

    # Returns current number of elements in set
    def get_size(self):

        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        for element in self.buckets:
            for val in element:
                if word == val:
                    return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        for element in self.buckets:
            for val in element:
                if word == val:
                    self.size -= 1
                    element.remove(val)
                else:
                    continue
        return self.buckets

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        count = 0
        for element in self.buckets:
            if len(element) > count:
                count = len(element)
            else:
                continue
        return count

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        count = 0
        for element in self.buckets:
            if len(element) == 0:
                count += 1
            else:
                continue
        return count / len(self.buckets)

    # Returns a list with all words in the set
    def as_list(self):
        newlst = []
        for element in self.buckets:
            for name in element:
                if len(element) != 0:
                    newlst.append(name)
        return newlst
