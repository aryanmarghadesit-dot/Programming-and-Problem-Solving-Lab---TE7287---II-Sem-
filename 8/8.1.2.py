start=int(input())
stop=int(input())
Flag=False
for n in range(start,stop+1):
	if(n>1):
		f=True
		for i in range(2,n):
			if(n%i == 0):

				f=False
				break
		if(f):
			print(n)
			Flag =True
if not Flag:
	print("No primes")
