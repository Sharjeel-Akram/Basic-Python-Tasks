#Write a python program which takes the name of a fruit as input from the user and check its existence.

myFruits = ['peach','Banana','pomegranate','Apple','Mangoes']
print(myFruits)
FruitName=input('Enter Fruit Name:')
if FruitName in myFruits:
    print(FruitName,'is exist')
    print('The index of fruit in list is:',myFruits.index(FruitName))
else:
    print(FruitName,'does not exist')
