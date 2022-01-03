""" 
what happen in case of range if you run in comman prompt

>>> range (1,10)
range(1, 10)
>>> r = range(1,10)
>>> list(r)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list[r]
list[range(1, 10)]
>>> range (1,10,2)
range(1, 10, 2)
>>> list[r]
list[range(1, 10)]
>>> list(r)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> range(3)
range(0, 3)
>>> list(r)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> r= range(3)
>>> list(r)
[0, 1, 2]

"""

for x in range(1,7):
	print (x)

for y in range(7,0,-1):
	print (y)

for z in range(10):
	print (z)

num=(1,10)
print (num)