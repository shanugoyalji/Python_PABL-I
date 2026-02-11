#You are given an array of integers arr[]. You have to reverse the given array.

class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        
        # Iterate only through the first half of the array
        for i in range(n // 2):
            # Calculate the opposite index
            opposite_index = n - 1 - i
            
            # Swap elements in-place
            arr[i], arr[opposite_index] = arr[opposite_index], arr[i]
            
        return arr
