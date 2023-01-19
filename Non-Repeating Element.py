#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        for i in range(0,n):
            cnt = 0
            for j in range(0,n):
                if arr[i] == arr[j]:
                    cnt = cnt + 1
                    if cnt == 2:
                        break
            if cnt == 1:
                return arr[i]
