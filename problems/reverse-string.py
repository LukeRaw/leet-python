# Reverse a string

# My solution
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Loop until half way is reached
        for i in range(int(len(s)/2)):
            # Exchange items at either end of the list
            tmp = s[-1-i]
            s[-1-i] = s[i]
            s[i] = tmp  


# Solution from discussion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize the left and right pointers
        left, right = 0, len(s) - 1
        
        # Loop until the pointers meet at the center
        while left < right:
            # Swap the characters at the left and right indices
            s[left], s[right] = s[right], s[left]
            
            # Increment left and decrement right
            left += 1
            right -= 1