#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        l = []
        flag = 0
        for i in pat:
            x = Str.find(i)
            if x >= 0:
                flag = 1
            if flag == 1 and x >= 0:
                l.append(x)
        if flag == 1:
            return min(l)
        else:
            return x

