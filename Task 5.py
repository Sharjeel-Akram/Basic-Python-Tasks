#Write a python program which takes names of 5 fruits as input from the user and stores in List.

myFruits = []
for i in range(5):
    fruits = input("Write the names of Your fruits:")
    myFruits.append(fruits)
print(myFruits)