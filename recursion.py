l = [13, 8, 7, 21, 19, 6]
def isinlist(l, n):
    if l[0] == []:
        return False
    elif l[0] == n or isinlist(l[1:], n):
        return True 
    
        
    
print(isinlist([13, 8, 7, 21, 19,6], 21))
