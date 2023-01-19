#User function Template for python3

class Solution:

    def printSequence(self,S):
        # code here
        s1 = ""
        for i in S:
            if i == 'A':
                s1 = s1 + '2'
            elif i == 'B':
                s1 = s1 + '22'
            elif i == 'C':
                s1 = s1 + '222'
            elif i == 'D':
                s1 = s1 + '3'
            elif i == 'E':
                s1 = s1 + '33'
            elif i == 'F':
                s1 = s1 + '333'
            elif i == 'G':
                s1 = s1 + '4'
            elif i == 'H':
                s1 = s1 + '44' 
            elif i == 'I':
                s1 = s1 + '444' 
            elif i == 'J':
                s1 = s1 + '5' 
            elif i == 'K':
                s1 = s1 + '55'
            elif i == 'L':
                s1 = s1 + '555' 
            elif i == 'M':
                s1 = s1 + '6' 
            elif i == 'N':
                s1 = s1 + '66' 
            elif i == 'O':
                s1 = s1 + '666' 
            elif i == 'P':
                s1 = s1 + '7'
            elif i == 'Q':
                s1 = s1 + '77'
            elif i == 'R':
                s1 = s1 + '777'
            elif i == 'S':
                s1 = s1 + '7777'
            elif i == 'T':
                s1 = s1 + '8'
            elif i == 'U':
                s1 = s1 + '88'
            elif i == 'V':
                s1 = s1 + '888' 
            elif i == 'W':
                s1 = s1 + '9' 
            elif i == 'X':
                s1 = s1 + '99' 
            elif i == 'Y':
                s1 = s1 + '999'
            elif i == 'Z':
                s1 = s1 + '9999' 
            else:
                s1 = s1 + '0'
        return s1

