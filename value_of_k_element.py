#Given an integer array arr[] and an integer k, your task is to find and return
the kth smallest element in the given array.

class Solution:
    def kthSmallest(self, arr, k):
        # Step 1: Sort the array in ascending order
        arr.sort()
        
        # Step 2: Return the element at index k-1
        return arr[k - 1]
