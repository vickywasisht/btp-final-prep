class HashTable:
    def __init__(self, size):
        self.m = size
        self.T = [None] * size

    def insert(self, data):
        i = 0
        while i < self.m:
            # calculate the hash value of the key
            idx = hash(data.key, i)
            # is key available
            if self.T[idx] == None:
                # it is so go in and return
                self.T[idx] = data
                return 
            else:
                i = i + 1
        raise "Full Table"

    def search(self, key):
        i = 0
        while i < self.m:
            idx = hash(key, i)
            if self.T[idx] == key:
                # Found key
                return self.T[idx]
            elif self.T[idx] == None:
                # key not in table
                return None
            i = i + 1