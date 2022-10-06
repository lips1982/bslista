import random


lista=[1,2,3,4,5,6]
elem=lista.pop(random.randrange(len(lista))) 
print(elem, lista)
elem=lista.pop(random.randrange(len(lista))) 
print(elem, lista)
elem=lista.pop(random.randrange(len(lista))) 
print(elem, lista)
elem=lista.pop(random.randrange(len(lista))) 
print(elem, lista)

"CANCIONA1"

mylistartistas=[]

mylistartistas.append("CANCIONA1")
mylistartistas.append("CANCIONA1")
mylistartistas.append("CANCIONA1")
mylistartistas.append("CANCIONA1")
mylistartistas.append("CANCIONA2")
mylistartistas.append("CANCIONA2")
mylistartistas.append("CANCIONA2")
mylistartistas.append("CANCIONA2")
mylistartistas.append("CANCIONA3")
mylistartistas.append("CANCIONA3")
mylistartistas.append("CANCIONA3")
mylistartistas.append("CANCIONA3")
            
mylistartistas =random.sample(mylistartistas, 12)

print (mylistartistas)

