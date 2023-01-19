#User function Template for python3



def maxArea(A,le):
    #code here
    l = max(A)
    l1 = l
    a = []
    for i in range(0,len(A)):
        l = l - 1
        if l in A:
            b = l1 - l
            c = min(l,l1)
            d = c * b
            a.append(d)
    return (max(a))
