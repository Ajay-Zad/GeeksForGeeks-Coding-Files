#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        s1 = ""
        s2 = ""
        s1 = str1
        s1 = str1[2:] + str1[0:2]
        s2 = str1[len(str1)-2:] + str1[:len(str1)-2]
        
        if s1 == str2 or s2 == str2:
            return 1
        else:
            return 0