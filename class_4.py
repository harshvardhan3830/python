# for i in range(3):
#     print("Value of i is =====>>>>>",i)
# else:
#     print("Loop finished")

#While

# i = 3
# while i <=10:
#     print("Value of i => ", i)
#     i += 1
# else:
#     print("Loop finshed") 


#Loop control statements
# break, continue, pass

# for i in range(5):
#     if( i == 3):
#         # break
#         # continue
#         pass
#     print("value if i is ", i)

# print("Loop breaked!")


# Star pattern

# *
# **
# ***
# ****
# *****

# rows = int(input("Enter number of rows ==>> "))
# for i in range(rows):
#     print("*" * (i+1))


# *****
# ****
# ***
# **
# *

# rows = 5
# for i in range(rows, 0, -1):
#     print(" * " * i)


#    *  
#   * *  
#  * * *  
# * * * *


rows = 4
for i in range(1, rows+1):
    print( " " * (rows-i) + "* " * i)