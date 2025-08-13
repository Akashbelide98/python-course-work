'''import sys
print(sys.argv)'''

'''import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.processor())'''


import math
print(math.pi)      # Output: 3.141592653589793
print(math.e)       # Output: 2.718281828459045
print(math.sqrt(25))  # Output: 5.0
print(math.pow(3,3))  # Output: 27.0

print(round(12.3)) # Output: 12
print(round(12.8)) # Output: 13
print(math.ceil(25.3))  # Output: 26
print(math.ceil(25.8))  # Output: 26
print(math.ceil(25.00001))  # Output: 26

print(math.floor(25.3))  # Output: 25
print(math.floor(25.3))# Output: 25
print(math.floor(25.3)) # Output: 25


print(abs(-13))  # Output: 13
print(abs(-13.5))  # Output: 13.5

print(math.fabs(-13.5))  # Output: 13.5
print(math.factorial(5))  # 120
print(math.gcd(8,12)) #4 

print(math.log(2))#0.6931471805599453
print(math.log(2,2))#1.0
print(math.sin(45))#0.8509035245341184
print(math.cos(45))#0.5253219888177297
print(math.tan(45))#1.6197751905438615

print(math.degrees(45)) #2578.3100780887044
print(math.radians(45)) #0.785398163397448  







#random

import random

print(random.random())    #0.02367489149445756                      
print(random.randint(1,10)) #6
print(random.uniform(1,5)) #4.768436940150632

l=['afrin','kerthana','revathi','meghana','nihitha']

print(random.choice(l))
#print(random.choice(l,k=2))

print(l)
random.shuffle(l)
print(l)




#4.2 itertools
from itertools import combinations,permutations
s = 'abc'
t=tuple(combinations(s,2))
p = tuple(permutations(s,3))

for i in t:
    print(''.join(i),end=',')







'''n1=int(input())
n2=int(input())

n = min(n1,n2)

for i in range(n,0,-1):'''
