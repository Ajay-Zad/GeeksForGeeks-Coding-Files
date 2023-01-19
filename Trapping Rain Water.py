
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        cnt = 0
        h = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= h:
                cnt = cnt + (h-arr[i])
            else:
                h = arr[i]
        
        i = 0 
        s = 0
        if arr[0] < h:
            while arr[i] != h:
                if arr[i] >= s:
                    s = arr[i]
                cnt = cnt + (s-arr[i])
                cnt = cnt - (h-arr[i])
                i = i + 1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends