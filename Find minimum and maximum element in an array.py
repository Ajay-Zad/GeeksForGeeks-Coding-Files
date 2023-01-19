#User function Template for python3

def getMinMax( a, n):
    l = []
    mi = a[0]
    ma = a[0]
    for i in a:
        if i < mi:
            mi = i
        if i > ma:
            ma = i
    l.append(mi)
    l.append(ma)
    return l
    
    
    
