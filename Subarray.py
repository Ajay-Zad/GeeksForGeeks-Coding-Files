#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       for i in range(0,n):
            sum1 = 0
            for j in range(i,n):
                if sum1 <= s:
                    sum1 = sum1 + arr[j];
                    if sum1 == s:
                        return i+1,j+1
                else:
                    break
       else:
           arr = []
           arr.append(-1)
           return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends