#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    #code here
    try:
        i = s.find(x)
        return i
    except:
        return -1
