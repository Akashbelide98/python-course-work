Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p = "python programing'
SyntaxError: EOL while scanning string literal
>>> p = 'python programing'
>>> p.startswith('p')
True
>>> p.startswith('pyt')
True
>>> p.startswith('pyth')
True
>>> l = ['PFS22','PFS30','JFS21','DS','DA','PFS32','JFS31','AI','DS14','ML']
>>> for i in l:
	if i.startswith('PFS'):
		print(i)

PFS22
PFS30
PFS32
>>> l=['demo.png','operators.py','if.py','resume.pfd','image.jpg','functions.py']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in l
SyntaxError: invalid syntax
>>> if l.endswith('.py')
SyntaxError: invalid syntax
>>> print i
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> 
>>> for
SyntaxError: invalid syntax
>>> for i in ;
SyntaxError: invalid syntax
>>> for i in l
SyntaxError: invalid syntax
>>> l=['demo.png','operators.py','if.py','resume.pfd','image.jpg','functions.py']
>>> for i in l
SyntaxError: invalid syntax
>>> for in l:
	
SyntaxError: invalid syntax
>>> for i in l:
	if l.endswith('.py')
	
SyntaxError: invalid syntax
>>> for i in l:
	if l.endswith('.py'):
		print i
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in l:
	if l.endswith('.py'):
		print (i)

		
Traceback (most recent call last):

  File "<pyshell#35>", line 2, in <module>
    if l.endswith('.py'):
AttributeError: 'list' object has no attribute 'endswith'
>>> for i in l:
	for i.endswith('.py')
	
SyntaxError: invalid syntax
>>> for i in l:
	for i.endswith('.py'):
		
SyntaxError: invalid syntax
>>> for i in l:
	if i.endswith('.py'):
		print(i)

operators.py
if.py
functions.py
>>> "python".isalpha()
True
>>> 'python2.13'.isalpha()
False
>>> 'python@'.isalpha()
False
>>> 'python213'.isalnum()
True
>>> '313py'.isalnum()
True
>>> 'python'.islower()
True
>>> 'P'.islower()
False
>>> 'p123'.islower()
True
>>> ' '.isspace()
True
>>> 'python       '.isspace()
False
>>> '     '.isspace()
True
>>> 'python lang'.istitle()
False
>>> "Pyyhon Lang".istitle()
True
>>> 'myvar'.isidentifier()
True
>>> 'myvar'.isidentifier()
True
>>> '1myvar'.isidentifier()
False
>>> 'my-var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> 'my0var'.isidentifier()
True
>>> '5'.isdigit()
True
>>> 'l = python is best programmin lang'
'l = python is best programmin lang'
>>> l.replace('python','java')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.replace('python','java')
AttributeError: 'list' object has no attribute 'replace'
>>> AttributeError: 'list' object has no attribute 'replace'
SyntaxError: invalid syntax
>>> l = 'python is best programmin lang'
>>> l.replace('python','java')

'java is best programmin lang'
>>> l.replace('java','python')
'python is best programmin lang'
>>> p='pwd@123'
>>> p.maketrans('123@pwd','6512!@~')
{49: 54, 50: 53, 51: 49, 64: 50, 112: 33, 119: 64, 100: 126}
>>> p.translate(p.maketrans('123@pwd','6512!@~'))
'!@~2651'
>>> p.translate(str.maketrans('123@pwd','6512!@~'))
'!@~2651'
>>> l
'python is best programmin lang'
>>> l.split()
['python', 'is', 'best', 'programmin', 'lang']
>>> l.rsplit()
['python', 'is', 'best', 'programmin', 'lang']
>>> l.split('p')
['', 'ython is best ', 'rogrammin lang']
>>> l.split('i')
['python ', 's best programm', 'n lang']
>>> l.rsplit(' ',2)
['python is best', 'programmin', 'lang']
>>> l = ''''python
is
best
programmin
lang'''
>>> l.splitlines()
["'python", 'is', 'best', 'programmin', 'lang']
>>> l
"'python\nis\nbest\nprogrammin\nlang"
>>> l = ['python ', 's best programm', 'n lang']
>>> ''.join()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    ''.join()
TypeError: join() takes exactly one argument (0 given)
>>>  ''.join(l)
 
SyntaxError: unexpected indent
>>> ''.join(l)
'python s best programmn lang'
>>>  '&'.join()
 
SyntaxError: unexpected indent
>>> '&'.join()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    '&'.join()
TypeError: join() takes exactly one argument (0 given)
>>> '&'.join(l)
'python &s best programm&n lang'
>>> l=['python', 'is', 'best', 'programmin', 'lang']
>>> '&'.join(l)
'python&is&best&programmin&lang'
>>> '#$%&'.join(l)
'python#$%&is#$%&best#$%&programmin#$%&lang'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> 'p.ython.py',partition('.')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    'p.ython.py',partition('.')
NameError: name 'partition' is not defined
>>> 'p.ython.py'.partition('.')
('p', '.', 'ython.py')
>>> '1.python.py'.partition('.')
('1', '.', 'python.py')
>>> '1.python.py'.rpartition('.')
('1.python', '.', 'py')
>>> j='       xyz'
>>> j.strip()
'xyz'
>>> j.lstrip()
'xyz'
>>> j.rstrip()
'       xyz'
>>> j='     gjyh    junhj     '
>>> j.strip()
'gjyh    junhj'
>>> j.lstrip()
'gjyh    junhj     '
>>> j.rstrip()j='     gjyh    junhj     '
SyntaxError: invalid syntax
>>> j.rstrip()
'     gjyh    junhj'
>>> h = 'hello'
>>> h.encode()
b'hello'
>>> h.decode()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    h.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> teext = 'Hello $%&'
>>> teext.encode()
b'Hello $%&'
>>> b'Hello $%&'.decode()
'Hello $%&'
>>> 
