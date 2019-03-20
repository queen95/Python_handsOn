
def FirstFactorial(num):
    
    s =1
    while(num>0):
        s = s*num
        num = num -1
    return s    
    

#if __name__ == "__FirstFactorial__":
f = FirstFactorial( 4 )   
print(f)
print(FirstFactorial( 4 ))
