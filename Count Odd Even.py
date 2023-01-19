#User function Template for python3

class Solution:
    def countOddEven(self, arr, n):
        #Code here
        e = []
        o = []
        for i in arr:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        a = len(o)
        b = len(e)
        print(str(a)+" "+str(b))
