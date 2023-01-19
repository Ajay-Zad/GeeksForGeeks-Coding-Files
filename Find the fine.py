#User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        #Code here
        sum = 0
        if date % 2 == 0:
            for i in range(0,len(car)):
                if car[i] % 2 == 1:
                   sum = sum + fine[i] 
        else:
            for i in range(0,len(car)):
                if car[i] % 2 == 0:
                   sum = sum + fine[i] 
        return sum
            
            
    
    
    
