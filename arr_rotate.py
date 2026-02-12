# Given an array arr, rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, arr):
        n = len(arr)
        # Store the last element in a variable
        last_element = arr[n - 1]
        
        # Shift all elements to the right starting from the end
        # We use a reverse for-loop: range(start, stop, step)
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
            
        arr[0] = last_element
        
        return arr
