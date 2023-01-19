#User function Template for python3


class Solution:
    def findDuplicate(self, arr, N, K):
        s = set(arr)
        for i in s:
            if arr.count(i) == K:
                return i

