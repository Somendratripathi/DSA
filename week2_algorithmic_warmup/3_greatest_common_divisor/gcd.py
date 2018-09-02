# Uses python3
#import sys

def gcd_efficient(a, b):
    if a%b==0 or b==1:
        return(b)
    #print(a,b,"\n")      
    return(gcd_efficient(b,a%b))
    
    
    
    
if __name__ == "__main__":
    inp = input ()
    a, b = map(int, inp.split())
    if(b>a):
        b,a=a,b
    print(gcd_efficient(a, b))
  
    
