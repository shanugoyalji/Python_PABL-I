# Function to return the count of number of elements in union of two arrays.

class Solution:    

    def findUnion(self, a, b):
        union_set = set(a) | set(b)
        
        return list(union_set)
