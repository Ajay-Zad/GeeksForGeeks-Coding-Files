# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    s = ""
    for i in arr:
        s = s + str(i)
    s1 = s.count(str(k))
    return (s1)
        

