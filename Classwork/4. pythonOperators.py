'''#1. Arthemetic Operators
a = 20
b = 30
print('Addition(a+b):',a+b) #Addition(a+b): 50
print('subtraction(a-b):',a-b) #subtraction(a-b): -10
print('multiplication(a*b):',a*b)#multiplication(a*b): 600
print('division(a/b):',a/b) #division(a/b): 0.6666666666666666
print('Modulus(a%b):',a%b) #Modulus(a%b): 20
print('Expoential(a**b):',a**b) #Expoential(a**b): 1073741824000000000000000000000000000000'''

'''#2.Comparisom Operators
c=56
d=26
print('Equal to(c==d):',c==d) #Equal to(c==d): False
print('Not Equal to(c!=d):',c!=d) #Not Equal to(c!=d): True
print('Greater than(c>d):',c>d) #Greater than(c>d): True
print('Less than(c<d):',c<d) #Less than(c<d): False
print('Greater than or equal(c>=d)',c>=d) #Greater than or equal(c>=d) True
print('Less than or equal to(c<=d)',c<=d) #Less than or equal to(c<=d) False '''

'''#3.Assignment operator
x=20
print('x',x)
print('Addition Assignment:',x+5) #Addition Assignment: 25
print('subraction assingment:',x-5) #subraction assingment: 15
print('Multiplication assignmnet:',x*5) #Multiplication assignmnet: 100
print('Division assignment:',x/5) #Division assignment: 4.0
print(' floor Division assignment:',x//5) # floor Division assignment: 4
print('Modulus assignment:',x%5) #Modulus assignment: 0
print('Exponentiate assignment:',x**5) #Exponentiate assignment: 3200000'''


'''#4.Logical operators
print('Logical Operators')
x= 10
y=20

print('Logical And:',x>5 and x<40)
print('Logical or:',x > 15 or y < 30)
print('Logical Not:',not(x > 5))'''



'''#5.Membership operator
cities= ['Hyd', 'Bngl' 'del', 'Mum']
print ('Hyd' in cities)
print ('pune'in cities)
print ('goa' not in cities)


t=('car' ,'bike' , 'truck' , 'auto')
print ('car' in t)
print('ship' in t)
print('auto' not in t)
print('plane' not in t)

s={1,2,3,4,5,6,7,8,}
print(1 in s) #True
print (9 in s) #False
print (11 not in s ) #True
print (5 not in s) #False

Data = {"Name": "Akash", "Batch": 31, "City":"Hyd" }
print ("sai" in Data) #False
print (50 in Data) #False
print (50  not in Data) #True '''

'''#6. Identity Operators
x = [1, 2, 3]
y = x   # y is a reference to the same list as x
z = x.copy()  # z is a copy of the list x 
print('x is y:', x is y)  # True, because y references the same object as x
print('x is z:', x is z)  # False, because z is a different
print('x is not y:', x is not y)  # False, because y references the same object as x
print('x is not z:', x is not z)  # True, because z is a different object   
print('y is z:', y is z)  # False, because y and z are different objects
print('y is not z:', y is not z)  # True, because y and
# z are different objects
print('x is not y:', x is not y)  # False, because y references the same object as x
print('x is z:', x is z)  # False, because z is a different object
print('x is not z:', x is not z)  # True, because z is              
# a different object
print('y is not z:', y is not z)  # True, because y and
# z are different objects
print('y is z:', y is z)  # False, because y and z are different objects
print('y is not z:', y is not z)  # True, because y and         
# z are different objects
print('x is not y:', x is not y)  # False, because y references
# the same object as x'''


# #7. Bitwise Operators
a = 10  # 1010 in binary    
b = 4   # 0100 in binary

print('Bitwise AND (a & b):', a & b)  # Bitwise AND (a & b): 0
print('Bitwise OR (a | b):', a | b)   # Bitwise OR (a | b): 14
print('Bitwise XOR (a ^ b):', a ^ b)  # Bitwise XOR (a ^ b): 14
print('Bitwise NOT (~a):', ~a)         # Bitwise NOT (~a): -11
print('Left Shift (a << 2):', a << 2)  # Left   # Shift (a << 2): 40
print('Right Shift (a >> 2):', a >> 2)  # Right # Shift (a >> 2): 2 
print('Left Shift (b << 2):', b << 2)  # Left Shift (b << 2): 16
print('Right Shift (b >> 2):', b >> 2)  # Right # Shift (b >> 2): 1         
print('Bitwise AND (a & b):', a & b)  # Bitwise AND (a & b): 0
print('Bitwise OR (a | b):', a | b)   # Bitwise OR (a | b): 14
print('Bitwise XOR (a ^ b):', a ^ b)  # Bitwise XOR (a ^ b): 14
print('Bitwise NOT (~a):', ~a)         # Bitwise NOT (~a): -11      
print('Left Shift (a << 2):', a << 2)  # Left Shift (a << 2): 40
print('Right Shift (a >> 2):', a >> 2)  # Right Shift (a >> 2): 2               
print('Left Shift (b << 2):', b << 2)  # Left Shift (b << 2): 16
print('Right Shift (b >> 2):', b >> 2)  # Right Shift (b >> 2): 1       
print('Bitwise AND (a & b):', a & b)  # Bitwise AND (a & b): 0
print('Bitwise OR (a | b):', a | b)   # Bitwise OR (a | b): 14
print('Bitwise XOR (a ^ b):', a ^ b)  # Bitwise XOR (a ^ b): 14
print('Bitwise NOT (~a):', ~a)         # Bitwise NOT (~a): -11  
print('Left Shift (a << 2):', a << 2)  # Left Shift (a << 2): 40
print('Right Shift (a >> 2):', a >> 2)  # Right Shift (a >> 2): 2
print('Left Shift (b << 2):', b << 2)  # Left Shift (b << 2): 16                    
print('Right Shift (b >> 2):', b >> 2)  # Right Shift (b >> 2): 1     
print('Bitwise AND (a & b):', a & b)  # Bitwise AND (a & b): 0
print('Bitwise OR (a | b):', a | b)   # Bitwise OR (a | b): 14
print('Bitwise XOR (a ^ b):', a ^ b)  # Bitwise                                                

















