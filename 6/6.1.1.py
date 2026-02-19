days=int(input())
month=int(input())
year=int(input())
flag = True
if (year < 1 or month < 1 or month>12 ):
	flag = False

if( month in (1,3,5,7,8,10,12)):
	maxday=31
elif(month in (4,6,9,11)):
	maxday=30
else:
	if(year % 4 ==0):
		maxday = 29
	else:
		maxday =28

if (days > maxday or days <1):
	flag = False

days = days+1
if( days > maxday):
	days=1
	month=month+1
if( month > 12 ):
	month=1
	year =year+1

if(flag ):
	print(f"{days:02d}-{month:02d}-{year}")
else:
	print("Invalid Date")
