Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4,5,3]
>>> l
[1, 2, 3, 4, 5, 3]
>>> l.append(68)
>>> l
[1, 2, 3, 4, 5, 3, 68]
>>> l
[1, 2, 3, 4, 5, 3, 68]
>>> l(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l(3)
TypeError: 'list' object is not callable
>>> l[3]
4
>>> l[-1]
68
>>> l[1]
2
>>> l.append[2,3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l.append[2,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l.append(2,3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.append(2,3)
TypeError: append() takes exactly one argument (2 given)
>>> l.append(2.3)
>>> l.append(3+9j)
>>> l.append("string")
>>> l.append(True)
>>> l.append(['list1','list2'])
>>> l'append((1,2,3,4)}
SyntaxError: EOL while scanning string literal
>>> l.append(1,2,3,4)))
SyntaxError: invalid syntax
>>> l.append((1,2,3,4))
>>> l.append({4,5,6,6})
>>> l.append{{'key1':'val1','key2':'val2'}}
SyntaxError: invalid syntax
>>> l.append({'key1':'val1','key2':'val2')}
SyntaxError: invalid syntax
>>> l.append{{'key1':'val1','key2':'val2'}
	 
SyntaxError: invalid syntax
>>> l.append({'key1':'val1','key2':'val2'})
>>> l
[1, 2, 3, 4, 5, 3, 68, 2.3, (3+9j), 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}]
>>> l
[1, 2, 3, 4, 5, 3, 68, 2.3, (3+9j), 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}]
>>> l[3:7]
[4, 5, 3, 68]
>>> l{3:8}
SyntaxError: invalid syntax
>>> l{3:8}
SyntaxError: invalid syntax
>>> l[3:8]
[4, 5, 3, 68, 2.3]
>>> l[-1:-5]
[]
>>> l[-5:]
[True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}]
>>> l.extend([1,2,3,5])
>>> l
[1, 2, 3, 4, 5, 3, 68, 2.3, (3+9j), 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5]
>>> l[-5:]
[{'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5]
>>> l[-4:]
[1, 2, 3, 5]
>>> l[-9:-5]
[True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}]
>>>  l[-8:-5]
 
SyntaxError: unexpected indent
>>> l[-8:-5]
[['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}]
>>> l[-8:-4]
[['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}]
>>> l[::-1]
[5, 3, 2, 1, {'key1': 'val1', 'key2': 'val2'}, {4, 5, 6}, (1, 2, 3, 4), ['list1', 'list2'], True, 'string', (3+9j), 2.3, 68, 3, 5, 4, 3, 2, 1]
>>> l
[1, 2, 3, 4, 5, 3, 68, 2.3, (3+9j), 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5]
>>> l[8]
(3+9j)
>>> l[8]=13
>>> ll[8]=13
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ll[8]=13
NameError: name 'll' is not defined
>>> l[8]=13
>>> ;
SyntaxError: invalid syntax
>>> l
[1, 2, 3, 4, 5, 3, 68, 2.3, 13, 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5]
>>> l[7]=23
>>> l.append(83)
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5, 83]
>>> l.append(100)
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5, 83, 100]
>>> l.inser(9,20)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    l.inser(9,20)
AttributeError: 'list' object has no attribute 'inser'
>>> l,insert(9,20)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l,insert(9,20)
NameError: name 'insert' is not defined
>>> l.insert(9,20)
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 20, 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5, 83, 100]
>>> l.extend([16,17,18,19])
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 20, 'string', True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5, 83, 100, 16, 17, 18, 19]
>>> l.remove('string')
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 20, True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, {'key1': 'val1', 'key2': 'val2'}, 1, 2, 3, 5, 83, 100, 16, 17, 18, 19]
>>> l.remove({'key1':'val1','key2':'val2')
	 
SyntaxError: invalid syntax
>>> l.remove({'key1':'val1','key2':'val2'})
>>> l
[1, 2, 3, 4, 5, 3, 68, 23, 13, 20, True, ['list1', 'list2'], (1, 2, 3, 4), {4, 5, 6}, 1, 2, 3, 5, 83, 100, 16, 17, 18, 19]
>>> 
