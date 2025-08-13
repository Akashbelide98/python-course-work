#1
'''from collections import deque,defaultdict,Counter

s = 'Hello world Python Program'
feq = Counter(s)
print(feq)'''

#2
'''from collections import deque,defaultdict,Counter

s=[1,2,3,4,1,2,3,6,1,2,3,6,17,2,3,4,5]
d = defaultdict(int)
for i in s:
     d[i]+=1
print(d)'''


#3
'''from collections import deque,defaultdict,Counter
d = deque()
d.appendleft(12)
d.popleft()


d.append(34)
d.popleft()
d.appendleft(56)
d.append(78)
d.appendleft(90)  
d.popleft()
d.pop()  
print(d)'''


#4
from datetime import date,time,datetime,timedelta
today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())


print(date(2019,2,3))

print(time(3,6,6))

now = datetime.now()
print(now)