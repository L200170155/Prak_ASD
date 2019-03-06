Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cetaksiku(x):
    i=1
    while i<=x:
        print("*"*i)
        i+=1

        
>>> cetaksiku(3)
*
**
***
>>> 
>>> def gambarlahPersegiEmpat(a,b):
    i=1
    print("@"*b)
    while(i<a):
        print("@"+" "*(b-2)+"@")
        i+=1
        print("@"*b)

        
>>> gambarlahPersegiEmpat(5,5)
@@@@@
@   @
@@@@@
@   @
@@@@@
@   @
@@@@@
@   @
@@@@@
>>> 
>>> def jumlahhurufvokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return(vokal,jumlahhuruf)

>>> print(jumlahhurufvokal("afgi"))
(2, 4)
>>> 
>>> def jumlahhurufkonsonan(a):
	v="bcdfghjklmnpqrstvwxyz"
	konsonan=0
	jumlahhuruf=0
	for i in a:
		jumlahhuruf+=1
		if i in v:
			konsonan+=1
	return(konsonan,jumlahhuruf)

>>> print(jumlahhurufkonsonan("afgiii"))
(2, 6)
>>> 
>>> def rerata(b=[]):
	x=0
	n=0
	if b!=[]:
		for i in b:
			x+=1
			n+=1
		return x/n
	return "illegal"

>>> print (rerata([2,2]))
1.0
>>> 
>>> from math import sqrt as sq
>>> def apakahPrima(n):
	n=int(n)
	assert n>=0
	primakecil=[2,5,7,11]
	bukanprima=[0,1,4,6,8,9,10]
	if n in primakecil:
		return True
	elif n in bukanprima:
		return False
	else:
		for i in range(2,int(sq(n))+1):
			if(n%i==0):
				return False
			return True

		
>>> print(apakahPrima(71))
True
>>> 
>>> def cetakbilanganprima():
	prima=list()
	for i in range(2,100):
		a=True
		for iter in prima:
			if(i%iter==0):
				a=False
				break
		if(a):
			print(i)
			prima.append(i)

			
>>> cetakbilanganprima()
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>> 
>>> def faktorprima(n):
	prima=list()
	for i in range(2,n):
		a=True
		for iter in prima:
			if(i%iter==0):
				a=False
				break
			if a and n%i==0:
				prima.append(i)
			return prima

		
>>> print(faktorprima(143))
None
>>> 
>>> def apakahTerkandung(a,b):
	return a in b

>>> print(apakahTerkandung("db","abcdcdsqwedb"))
True
>>> print(apakahTerkandung("abd","abc"))
False
>>> 
>>> def iterasi():
	for i in range(1,100):
		if(i%3)!=0 and (i%5)!=0:
			print(i)
		else:
			if(i%15)==0:
				print("python UMS")
			elif(i%3)==0:
				print("python")
			elif(i%5)==0:
				print("UMS")

				
>>> iterasi()
1
2
python
4
UMS
python
7
8
python
UMS
11
python
13
14
python UMS
16
17
python
19
UMS
python
22
23
python
UMS
26
python
28
29
python UMS
31
32
python
34
UMS
python
37
38
python
UMS
41
python
43
44
python UMS
46
47
python
49
UMS
python
52
53
python
UMS
56
python
58
59
python UMS
61
62
python
64
UMS
python
67
68
python
UMS
71
python
73
74
python UMS
76
77
python
79
UMS
python
82
83
python
UMS
86
python
88
89
python UMS
91
92
python
94
UMS
python
97
98
python
>>> 
>>> def selesaikanABC(a,b,c):
	a=float(a)
	b=float(b)
	c=float(c)
	D=(b**2)-(4*a*c)
	if D<0:
		return "determinan negatif"
	return "determinan positif"

>>> print(selesaikanABC(1,1,2))
determinan negatif
>>> 
>>> def apakahkabisat(a):
	if(a%400==0):
		return True
	if(a%100==0):
		return False
	if(a%4==0):
		return True
	return False

>>> print(apakahkabbisat(100))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(apakahkabbisat(100))
NameError: name 'apakahkabbisat' is not defined
>>> print(apakahkabisat(100))
False
>>> 
>>> import random
>>> def permainan():
	a=random.randrange(0,100)
	while(True):
		b=int(input("masukkan angka: "))
		if(b>a):
			print("terlalu besar, coba lagi")
		elif(b<a):
			print("terlalu kecil, coba lagi")
		else:
			print("benar")
			break

		
>>> permainan()
masukkan angka: 20
terlalu kecil, coba lagi
masukkan angka: 105
terlalu besar, coba lagi
masukkan angka: 0
terlalu kecil, coba lagi
masukkan angka: 100
terlalu besar, coba lagi
masukkan angka: 
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    permainan()
  File "<pyshell#53>", line 4, in permainan
    b=int(input("masukkan angka: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> def formatRupiah(a):
	b=str(a)
	c=""
	i=-1
	while i>=-len(b):
		if((i+1)%3==0 and (i+1)!=0):
			c="."+c
			c=b[i]+c
			i-=1
		return "Rp "+c

	
>>> print(formatRupiah(30000000))
Rp 
>>> 
>>> 
