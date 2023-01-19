#User function Template for python3

class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        s = set(arr)
        for i in s:
            if i in arr:
                arr.remove(i)
        l = list(s)
        arr1 = l + arr
        cnt = 0
        for i in range(len(s),len(arr1)):
            a = 0
            b = arr1[i]
            while a != 1:
                if b in arr1:
                    cnt = cnt + 1
                    b = b + 1
                else:
                    a = 1
                    arr1.append(b)
        return (cnt)
