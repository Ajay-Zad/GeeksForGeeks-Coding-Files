#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # code here
    a = x - 1
    b = x + 1
    l = []
    if a in arr:
        l.append(a)
    else:
        l.append(-1)
    
    if b in arr:
        l.append(b)
    else:
        l.append(-1)
    return l