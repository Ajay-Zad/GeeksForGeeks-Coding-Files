#User function Template for python3
class Solution:

    
    def search(self,arr, n, k): 
        # code here
        try:
            s = arr.index(k)
            return s+1
        except:
            return -1
        

