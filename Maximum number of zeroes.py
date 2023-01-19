# User Template code

def MaxZero(arr, n):
    # Your code goes here
    cnt = 0
    l = []
    for i in arr:
        ii = str(i)
        iii = ii.count('0')
        if iii >= cnt:
            cnt = iii
            l.append(i)
            
    if cnt == 0:
        return -1
    else:
        ll = []
        for i in l:
            if str(i).count('0') == cnt:
                ll.append(i)
        return(max(ll))
        