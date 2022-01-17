#Write a python program which takes a number as input from the user and check its existence. 


myList=[1,2,3,4,5,6,7,8,9,10,11,12]
Number=int(input("Enter a number:"))
if Number in myList:
    print(Number,'is exist in the list')
    print('The index of given number is:',myList.index(Number))
else:
    print(Number,'does not exist')

