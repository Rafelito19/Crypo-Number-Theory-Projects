
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
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
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

   

bound=100000
n=2
while n < bound:
  passedtest = chtest(n)
  if passedtest == True and traildb(n) == False: 
  	    print (n,"passed the chinese test but it is not prime")
     
 
  n=n+1
   

  

