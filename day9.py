'''
Nested loop
Pattern programs
'''
'''
******
******
*****
****
***
***
****
'''

# simple


# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")

# print("******\n******\n******\n******")


# print("*****\n"*5)

'''
for i in range(5):
    print("******")
'''

'''
*****
*****
*****
*****
*****
'''

for i in range (1,6):
    for j in range(1,6):
        print("*",end='')
    print()


'''
*
**
***
****
*****
'''

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()


'''
    *
   **
  ***
 ****
*****
'''

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print('*',end="")
    print()


'''
    *
   * *
  * * *
 * * * * 
* * * * *

'''


for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print('* ',end="")
    print()