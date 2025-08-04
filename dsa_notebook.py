#REVERSE A ARRAY IN PYTHON. -- GFG (https://www.geeksforgeeks.org/problems/reverse-an-array/1)
class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        for i in range(n//2):
            arr[i]=arr[i]^arr[n-i-1]
            arr[n-i-1]=arr[i]^arr[n-i-1]
            arr[i]=arr[i]^arr[n-i-1]


#CHECK IF STRING IS PALINDROME OR NOT -- LEETCODE (https://leetcode.com/problems/valid-palindrome/)
class Solution(object):
    def isPalindrome(self, s):
        res=""
        for i in s:
            if i.isalpha():
                res+=i
        res=res.lower()
        reverse=res[::-1]
        return res==reverse


#MAX ELEMENT IN AN ARRAY -- VSCODE SELF
array = [1,2,5,8,2,11,6,5,22,56,0,-21,-100]
max=array[0]
for i in array:
    if i>max:
        max=i
print("Max Value in Array is:", max)


#COUNT VOWELS IN A STRING -- SELF VSCODE
string="Hello world Im jeet, Are you Earth"
count=0
string=string.lower()
for i in string:
    if i in ['a','e','i','o','u']:
        count+=1
print("Vowels:",count)


#CHECK IF THE ARRAY IS SORTED OR NOT.
for i in range(len(array)-1):
    if(array[i]>array[i+1]):
        print("False")
        exit()
print("True")

