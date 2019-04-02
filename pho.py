from fractions import gcd
import math

#based on wikipedia article"""

def pollard(n):  
	d=1
    
	x=2
	xf=2
	cs=100
	while d == 1:
		counter=1
		while counter <= cs and d <=1:
			x= (x*x + 1) %n
			d= gcd (abs(x-xf),n)
			counter = counter +1
		cs *= 2
		xf =x

		
	return d
		
			


fh= (2 ** 64) + 1
th = (2 **fh) +1
print (th)

print (pollard(fh))