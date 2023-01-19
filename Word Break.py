#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    for i in range(0,len(dictionary)):
        for j in range(i+1,len(dictionary)):
             s = s + dictionary[i] + dictionary[j]

    for i in line:
       if i not in s:
           return 0
    else:
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        dictionary = [word for word in input().strip().split()]
        line = input().strip()
        res = wordBreak(line, dictionary)
        if res:
            print(1)
        else:
            print(0)
# } Driver Code Ends