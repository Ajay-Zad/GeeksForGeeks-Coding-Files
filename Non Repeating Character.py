#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        l = list(s)
        for i in l:
            if l.count(i) == 1:
                return i
        else:
            return '$'
    
    
