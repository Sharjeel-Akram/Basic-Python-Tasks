#Write a Python program to generate random numbers from 1 to 20 and append them in list.
import random
newList=[]
for i in range(0,20):
    newList.append(i)
random.shuffle(newList)
print(newList)
