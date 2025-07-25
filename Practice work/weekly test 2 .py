'''#1
date,month,year=input("enter ").split('-')
print(f"{year}/{month}/{date}") # 2022/12/31'''

'''#2
n = int(input())
if n % 2 ==0:
    print('Even winner')
else:
    print('odd winner')'''

#3
'''n = input()
vol ='aeiouAEIOU'
for i in n:
    if i in vol:
        n = n.replace('i', "*")
print(n)'''

'''n= input()
print(n.translate(str.maketrans('aeiouAEIOU', '**********')))'''



#4
n = list(map(float,input())).split()
print(sum(n))
print(max(n))
