products ={
        "Apple":30,
        "Banana":10,
        "Orange":20,
        "Milk":50,
        "Bread":25,
        "Eggs":60,
        "Rice":40,
        "Tea": 35,
        "Sugar":20,
        "Salt":15  
      }
AddtoCart={}
while True:
    print("Available products".center(10," "))
    for i,key in enumerate(products):
        print(f'{i+1}.{key.ljust(10," ")}:${products[key]}')

        product=input('Enter the product name(Done-Exit):').title()
        if product=='Done':
            if AddtoCart:
                totalbill=0
                for i in AddtoCart:
                    print(f'{i.ljust(10," ")}:{AddtoCart[i]} * {products[i]}')
                    totalbill=totalbill+AddtoCart[i]*products[i]
                    print(f'Total Bill: {totalbill}')
            else:
                  print('Thanks')
            break
        if product in products:
            quantity=int(input(f'Enter the quantity of : '))
            if product in AddtoCart:
                AddtoCart[product]+=quantity
            else:
                AddtoCart[product]=quantity                                                                                                                                                                                                                                                                                                                                                                                                                                             

















int =input("Enter the product name:")
if int in products:
    print(f"The price of {int} is {products[int]} rupees.") 
else:
    print(f"{int} is not available in the store.")