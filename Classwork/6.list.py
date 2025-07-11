l=[1,2,3,'c','g',(1,2,3),[7,0,9],{'a':1,'b':2},'python','akash']
print(l)
print(l[0])  # Accessing the first element
print(l[3])  # Accessing the fourth element
print(l[6])  # Accessing the seventh element    
print(l[8])  # Accessing the ninth element
print(l[2:5])  # Slicing from index 2 to 4      
print(l[1:8])  # Slicing from index 1 to 7
print(l[:5])  # Slicing from index 0 to 4
k=[1,2,3,'gyghwdh']
print(k)
p=list()
print(p)
print(type(l))  # Checking the type of l    
print(type(k))  # Checking the type of k
print(type(p))  # Checking the type of p            
print(l[0:5])  # Slicing from index 0 to 4
print(l[2:8])  # Slicing from index 2 to 7                              ]
print(l[3:])  # Slicing from index 3 to the end
print(l[1:6:2]) 
print(l[:20:1])
l[2]=100
print(l) # Modifying the third element
l[1:3]=[300,200]
print(l) # Modifying the second and third elements
l[1:3]=[300,200,400]
print(l) # Modifying the second and third elements with more elements
print(l.count(1))
print(l.append(1000))
print(l)
l.insert(2, 500)
print(l)  # Inserting 500 at index 2
l.remove(500)   # Removing the first occurrence of 500
print(l)  # After removing 500  
l.pop(2)  # Removing the element at index 2
print(l)  # After popping the element at index 2    
l.extend([100, 200, 300])  # Extending the list with new elements
print(l)  # After extending the list
l.index('c')
print(l.index('c'))  # After finding the index of 'c'
print(k.clear())  # Clearing the list
print(k)  # After clearing the list
del l[0]
print(l)
l.remove('g')
print(l)
l.pop()
print(l)
#l.reverse()  # Reversing the list
print(l)  # After reversing the list    
l.pop(3)
print(l)  # After popping the element at index 3 
