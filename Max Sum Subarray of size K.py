Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

 

Example 1:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.
 

Example 2:

Input:
N = 4, K = 4
Arr = [100, 200, 300, 400]
Output:
1000
Explanation:
Arr1 + Arr2 + Arr3  
+ Arr4 =1000,
which is maximum.
 
SOLUTION :
  
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        if N == K:
            return sum(Arr)
        else:
            s = 0
            i = 0
            s1 = []
            while i < N-1:
                s1 = Arr[i:K]
                s2 = sum(s1)
                if s2 > s:
                    s = s2
                i = i + 1
                K = K + 1
            return s

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
 

  
Your Task:

You don't need to read input or print anything. Your task is to complete the function maximumSumSubarray() which takes the integer k, vector Arr with size N, containing the elements of the array and returns the maximum sum of a subarray of size K.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 


Constraints:
1<=N<=106
1<=K<=N
