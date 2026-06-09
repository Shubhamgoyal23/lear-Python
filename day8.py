'''
while loop
Syntax:-

initilization
while condition:
    statements
    incr/decr
'''

a = 1
while a<5:
    print("hello")
    a = a+1


# WAP to print 2 table 
a = 2
while a<=20:
    print(a)
    a =a+2


a = 5 
while a<=50:
    print(a)
    a=a+5

num =int(input("Enter any number: "))
a = 1
while a<=10:
    print(a*num)
    a = a+1


choice = "Y"
while choice in "Yy":
    name = input("Enter your name: ")
    mob= input("Enter your mob no: ")
    choice = input("Do you want to continue(Y/N): ")


# WAP to add all digits of a number 
# 754 => 7+5+4 => 16

add = 0
num = int(input("Enter a number: "))
while num >0:
    rem  = num%10
    add = add+rem
    num = num//10
    print("Addtion of all digits:",add)
    