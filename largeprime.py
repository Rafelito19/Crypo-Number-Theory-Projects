
def simplemodu(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y


def traildb(num):
    """
    Trail divisiton for referrance
    """

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False


    for i in range(3, int(num ** 0.5) + 2, 2):
        if num % i == 0:
            return False
    
    return True

def  grcd(a, b):
    """Calculate the graetest common divisor of a and b.

    """
    while b:
        a, b = b, a%b
    return a


 

def chtest(num):
    """
  Ancient chinese method 
    """
    a = 2
    if (grcd(a,num)) != 1:
        return False
    if simplemodu(a,num-1,num) != 1:
        return False
    

    return True

   
def miller_rabin(number, iterations):
     n= 0    
     while n < iterations: 


bound=1
n=2


print ( "2 ^500",chtest( 2 ** 500 ))

while n < bound:

     
 
  n=n+1
   

  

