#conditionals stmts
#1.simple if statement
'''hr,mins = list(map(int,input("enter the HH:MM : ").split(':')))

if hr>=0 and hr<=24 and mins>0 and mins<=60:
    if hr>=0 and hr<4:
        print("Its high timr,Time to sleep")
    elif hr>=4 and hr<12:
        print("Good Morning. Hve a nice day")
    elif hr>=12 and hr<16:
        print('Good Afternoon. Have a great Lunch')
    elif hr>=16 and hr<20:
        print('Good Evening. Have some snacks')
    elif hr>=20 and hr<24:
        print('Good Night.Sweet Dreams')
else:
    print('Enter the proper input,your input is invalid')'''


'''#2.if else statement
seats={
    "L1":True,
    "L2":False,
    "L3":True,
    "L4":False,
    "L5":False,
    "U1":False,
    "U2":True,
    "U3":False,
    "U4":True,
    "U5":False,
}
seatno=input("Enter the seat no to check its avaliability:").upper()

if seatno in seats:
    if seats[seatno]:
        print("Already booked try with other number:")
    else:
        print("Seat is avaliable. Hurry up")
else:
    print("Enter the correct seat number:")'''

#3
'''data={
    'watch':{'discount':10,'brands':['Titan','Fastrack','Casio']},
    'facewash':{'discount':24,'brands':['Nivea','Pears','Himalaya']},
    'tops':{'discount':15,'brands':['Zara','H&M','max']},
    'shirts':{'discount':44,'brands':['Levis','peterengland','AllenSolly']},
    'Jeans':{'discount':54,'brands':['denim','roadster']}
}
print(data.keys())
pro=input("Enter the cats: ")
if pro in data:
    print(f"{data[pro]['discount']} % discount is going on for this brands: {data[pro]['brands']}")
          
else:
    print(f"Product is out of stock,please check with other products: {data.keys()}") '''

#4'
movie={
    'salar':{'kids':True},
    'rajarani':{'kids':True},
    'Kannapa':{'kids':False},
    'Masudha':{'kids' :False},
    'Arjunreddy':{'kids' :False},
    'Littlestars':{'kids':True}
}
