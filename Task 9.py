#Write a Python program that takes a list as input from user and swap its first and last value.



Sharjeel =  []
for i in range(10):
    number = int(input("enter your number:"))
    Sharjeel.append(number)
number = Sharjeel[0]
Sharjeel[0] = Sharjeel[i]
Sharjeel[i] = number
print(Sharjeel)
