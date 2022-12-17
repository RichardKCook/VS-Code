# import random

# random_integer =  random.randint(1,5)

# random_float = random.random()

# print(random_integer * random_float)



# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut"]

# new = ["Richardland", "Fakestate"]

# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# D=[4,5,6]
# E=[5,6,7]
# F=[6,7,8]
# G=[7,8,9]
# H=[8,9,0]
# I=[9,0,1]


# X = [A,B,C]
# Y = [D,E,F]
# Z = [G,H,I]

# List = [X,Y,Z]

# print(List[0])
# print(List[0][1])
# print(List[0][1][2])


# import math


# def AreaCalc(H, W):
#     SA = H*W
#     cans = math.ceil(SA/5)
#     print(f"Your surface area is {SA}")
#     print(f"You need {cans} cans of paint")

# Height = int(input("What's the height is your wall? "))
# Width = int(input("What's the width of your wall? "))

# AreaCalc(Height, Width)


# def PrimeCheck(num):
#     is_prime = True
#     for i in range(2,num):
        
#         if num%i == 0:
            
        
#             is_prime = False
            
#     if is_prime == True:
#         print("It's Prime")
#     else:  
#         print("It's not Prime")

# n=int(input("What number would you like to check? "))

# PrimeCheck(n)

def format_name(f_name,L_name):
    """Takes a first and last name and format it to return the title case version of the name"""
    formatFirst=f_name.title()
    formatLast=L_name.title()
    
    return f"{formatFirst} {formatLast}"
    

formated_string = format_name("richard","cook")

print(formated_string)
