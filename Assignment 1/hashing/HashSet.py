from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):

        wordval = 0
        hashval = 0
        for char in word:
            wordval += ord(char)
        hashval = wordval % len(self.buckets)
        return hashval

    # Alternative solution By Anton
        # wordval = 0
        # prime = 31

        # for i, char in enumerate(word):
        # wordval = (wordval + (ord(char) - ord('a') + 1) * (prime ** i))
        # # we use the position of the char as a multiplyer to the prime

        # return wordval

    # Doubles size of bucket list
    def rehash(self):  # define the 256 bucket limit
        # Create new list with double the size
        # For loop to take out hashnums and turn them back into ascii
        # Ascii % len newlist
        # append

        if len(self.buckets) < 256:
            newlst = [[] for i in range(2*len(self.buckets))]
            for element in self.buckets:
                for name in element:
                    if name is None:
                        continue
                    else:
                        wordval = 0
                        for char in name:
                            wordval += ord(char)
                        newlst[wordval % len(newlst)].append(name)
            self.buckets = newlst
        return self.buckets

    # Adds a word to set if not already added
    def add(self, word):
        if word in self.buckets[self.get_hash(word)]:
            return 0
        else:
            bucket = self.get_hash(word)
            self.buckets[bucket].append(word)
            self.size += 1
            if len(self.buckets) == self.size:
                self.rehash()
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
