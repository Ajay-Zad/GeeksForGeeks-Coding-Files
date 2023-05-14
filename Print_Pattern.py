class Solution:
    def pattern(self, N):
        # code here
        l = []
        k = 0
        N1 = N
        while True:
            if k == 0:
                l.append(N)
                N = N - 5
                if N <= 0:
                    k = 1
            else:
                l.append(N)
                N = N + 5
                if N1 == N:
                    l.append(N1)
                    return l

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
