#User function Template for python3


def find(arr,n,x):
    # code here
    l = []
    l1 = []
    try:
        for i in range(0,len(arr)):
            if arr[i] == x:
                l.append(i)
        l1.append(min(l))
        l1.append(max(l))
                
        return l1
    except:
        l1.append(-1)
        l1.append(-1)
        return l1

