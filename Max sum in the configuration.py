#User function Template for python3

def max_sum(a,n):
    x = a
    l = []
    i=0
    while i < len(x):
        k = 0
        sum1 = 0
        for j in x:
            pro = j * k
            sum1 = sum1 + pro
            k = k + 1
        x = x[1:len(x)] + x[:1]
        l.append(sum1)
        i = i + 1
    return max(l)
        


        