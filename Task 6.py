 # Write a Python program to count the number of fruits which have 4 or more characters in their names.
myFruits = []
count=0
for i in range(5):
    fruits = input("Write the names of Your fruits:")
    myFruits.append(fruits)
    if len(fruits)>=4:
        count=count+1
    else:
        count=count


print(myFruits)
print('Number of fruits having 4 or more characters are:',count)
