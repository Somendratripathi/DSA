# Uses python3


def gcd_efficient(a, b):
    if a%b==0 or b==1:
        return(b)
    #print(a,b,"\n")      
    return(gcd_efficient(b,a%b))
    
    
def lcm_efficient(a,b):
    return((float(a)/(gcd_efficient(a, b)))*b)
    
if __name__ == "__main__":
    inp = input ()
    a, b = map(int, inp.split())
    if(b>a):
        b,a=a,b
    if(a*b>10**10):
        i = int((lcm_efficient(a, b)))+1000
        while i:
            if(i%a==0 and i%b==0):
                print(i)
                break
            i=i-1
    else:
        print(int((lcm_efficient(a, b))))
    
