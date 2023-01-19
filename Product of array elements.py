#User function Template for python3

# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    pro = 1
    for i in arr:
        pro = pro * i
    return pro % mod
