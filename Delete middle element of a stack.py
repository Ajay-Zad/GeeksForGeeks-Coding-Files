#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s,S):
        # code here
        if S % 2 == 0:
            S = (S // 2)
            del s[S-1]
            return s
        else:
            S = (S // 2)
            del s[S]
            return s
            
        
        