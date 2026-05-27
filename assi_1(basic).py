#Basic Input & Print Questions 

#1. Write a program to print “Hello Python” on the

print("Hello Python")

#2. Take a name as input and print
name=input("Enter your name: ")
print("Welcome",name)

# 3. Take a number as input and print it.

no = int(input("Enter a number: "))
print(no)
         

#4. Take two numbers as input and print both numbers on separate lines.

no1 = int(input("Enter a 1 number: "))
no2 = int(input("Enter a 2 number: "))

print(f'''{no1}
{no2}''')

#5. Take a name and age as input and print: 
#My name is ___ and my age is ___ 


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and my age is {age}")


# Integer (int) Based Questions

#6. Take an integer as input and print its square.  

num = int(input("Enter any number: "))

print(f"The square of the {num} is: {num*num}")

#7. Take two integers as input and print their sum.

num1 = int(input("Enter any 1 number: "))
num2 = int(input("Enter any 2 number: "))


print(f"The sum of the {num1} and {num2} is: {num1+num2}")

#8. Take two integers and print:
#o Addition 
#o Subtraction 
#o Multiplication


num1 = int(input ("Enter any fisrt number: "))
num2 = int(input ("Enter any second number: "))

add = num1+num2
sub = num1-num2
mul = num1*num2

print(f"""The additon of {num1} and {num2} is : {add}
The Subtraction  of {num1} and {num2} is : {sub}
The mu;tiplication of {num1} and {num2} is : {mul}""")



#9. Take a number and print:  The number entered is <number> 
      
 
number = int(input("Enter a number: "))
print ("The number entered is",number)

#10. Take an integer and print its double.

number = int(input("Enter any number: "))
c = number + number
print(c)


#Mixed int & float Questions

#16. Take one integer and one float as input and print both. 

             
int_num = int(input("Enter any number: "))
float_num  = float(input("Enter any deciaml number: "))

print (int_num,float_num)


#17. Take total marks (int) and number of subjects (int) and print the average as float.

marks = int(input("Enter your total marks: "))
sub =  int (input("Enter your total subject: "))
presenteg = float(marks/sub)

print("The average of your:", presenteg)


#18. Take price (float) and quantity (int) and print the total cost.

price = float(input("Enter the total price: "))
quan = int(input("Enter the total quanity: "))
total_cost = price*quan

print("The total bill is:", total_cost)


