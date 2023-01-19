#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        l = []
        l = a + b
        cnt = 0
        s = set(l)
        for i in s:
            if i in a and i in b:
                cnt = cnt + 1
        return (cnt)
                
        
        #code here
