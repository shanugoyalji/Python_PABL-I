# Given an array arr[]. The task is to find the largest element and return it.

class Solution:
    def largest(self, arr):
        max_element = arr[0]
        
        for i in range(1, len(arr)):
             if arr[i] > max_element:
                max_element = arr[i]
                
        return max_element
