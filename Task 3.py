# 3.	Write a program to sum all the odd numbers 
myList=[]
oddNumbers = []
SumOfOddNumbers=0
for i in range(10):
    number=int(input("Enter A Number:"))
    myList.append(number)
    if number % 2 != 0:
       oddNumbers.append(number)
       SumOfOddNumbers=SumOfOddNumbers+number
print('The List is:',myList)
print('The odd integers in the List is:',oddNumbers)
print('The Sum Of Odd Numbers In The List Is:',SumOfOddNumbers)