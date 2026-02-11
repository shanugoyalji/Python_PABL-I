#Given an array arr[]. Your task is to find the minimum and maximum elements
in the array.

class Solution:
    def getMinMax(self, arr):
        # Initialize min and max with the first element
        mini = arr[0]
        maxi = arr[0]
        
        # Iterate through the array
        for i in range(1, len(arr)):
            if arr[i] < mini:
                mini = arr[i]
            if arr[i] > maxi:
                maxi = arr[i]
        
        # GFG usually expects a list or tuple [min, max]
        return mini, maxi
