#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        try:
            a = arr.index(X)
            return a
        except:
            return -1
