# Uses python3
def gcd_efficient(a, b):
    if a%b==0 or b==1:
        return(b)
    #print(a,b,"\n")      
    return(gcd_efficient(b,a%b))
    
    
def lcm_efficient(a,b):
    return(a*b)/gcd_efficient(a, b)
    
if __name__ == "__main__":
    inp = input ()
    a, b = map(int, inp.split())
    if(b>a):
        b,a=a,b
    print(int(lcm_efficient(a, b)))