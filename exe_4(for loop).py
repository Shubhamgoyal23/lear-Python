'''
basic for loop q
'''
'''
# 1. print number 1to10

for i in range (1,11):
    print(i)               # line by line

    # or

print(*range(1,11))        # all in one line


# 2. print even numbers only 1 to 20
# even 2,4,6,8 odd 1,3,5,7,9

for i in range(2,21,2):
    print(i)

    
# 3.find sum 1 to 10

sum = 0

for i in range(1, 11):
    sum += i

print("Sum =", sum)

Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.

num = int(input("Enter any number; "))
for i in range(1,11):
   print(num,"*",i,"=",num*i)


Q5. Count Characters 
Take a string and count the total number of characters using a for loop. 


text = input("Enter a string: ")

count = 0

for char in text:
    count += 1

print("Total characters:", count)


Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5. 


for i in range(1,11):
    if i == 5:
        break
    print(i)


#or

for i in range(1,11):
    if i == 6:
        break
    print(i)



Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop. 



num  = int(input("Enter a number to search: "))
li =[20,24,48,85,25,96,68]

for i in li:
    if i == num:
        print("Found")
        break
    print(i)
    
Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.


li =[25,14,36,96,85,74,-58,54,56,92]
for i in li:
    print(i)
    if i < 0:
        print("The Negative Number is Found")
        break


Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.


for i in range(1,11):
    if i == 5:
        continue
    print(i) 

# with input
num = int(input("Enter a Number To Skip: "))

for i in range(1,11):
    if i == num:
        continue
    print(i)


Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers. 


# simple
for x in range(1,21,2):
    print(x)




for i in range(1,21):
    if i%2==0:
        continue
    print(i)



Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O". 



st = "PYTHON"

for i in st:
    if i == "O":
        continue
    print(i)


Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass. 


for i in range(1,11):
    if i == 6:
        pass
    print(i)
    

14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found". 
'''



li = [10,20,30,40,50,60,100,70,80,90]

for i in li:
    print(i)
    if i == 100:
        print("Found")
        break
else:
    print("Not Found")





