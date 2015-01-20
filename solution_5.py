# Prime number

import math
n=int(input("Please enter a natural number to test if it's prime: "))
def prime(x):
	if x < 2:
		return False
	elif x == 2:
		return True
	else: 
		nsqrt = int(math.sqrt(x))
		if nsqrt < 2: 
			return True
		else:
			for n in range(2, nsqrt+1):
				if x % n == 0: 
					return False 
			return True

print(prime(n))


