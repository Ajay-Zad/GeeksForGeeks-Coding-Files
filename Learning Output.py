#User function Template for python3

class Solution:
    def Learning(self, arr, n):
        # Your code goes here
        # return (0.1, 0.2, 0.3);
        p = 0
        n1 = 0
        o = 0
        for i in arr:
            if i > 0:
                p = p + 1
            elif i < 0:
                n1 = n1 + 1
            else:
                o = o + 1
        l = []
        a = n / p
        a1 = n % p
        if a1 == 0:
            l.append(int(a))
        else:
            l.append(round(a,5))
        b = n / n1
        b1 = n % n1
        if b1 == 0:
            l.append(int(b))
        else:
            l.append(round(b,5))
        c = n / o
        c1 = n % o
        if c1 == 0:
            l.append(int(c))
        else:
            l.append(round(c,5))
        return l
                