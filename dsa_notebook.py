#REVERSE A ARRAY IN PYTHON. -- GFG (https://www.geeksforgeeks.org/problems/reverse-an-array/1)
class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        for i in range(n//2):
            arr[i]=arr[i]^arr[n-i-1]
            arr[n-i-1]=arr[i]^arr[n-i-1]
            arr[i]=arr[i]^arr[n-i-1]
        
        
        
