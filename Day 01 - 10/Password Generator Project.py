#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))-1 
nr_symbols = int(input(f"How many symbols would you like?\n"))-1
nr_numbers = int(input(f"How many numbers would you like?\n"))-1

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
i=0
while i <= nr_letters:

    rand = random.randint(0,len(letters)-1)
    password += letters[rand]
    i += 1
i=0
while i <= nr_numbers:
    rand = random.randint(0,len(numbers)-1)
    password += numbers[rand]
    i += 1
i=0
while i <= nr_symbols:
    rand = random.randint(0,len(symbols)-1)
    password += symbols[rand]
    i += 1

print(password)
    


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print ("".join(random.sample(password,len(password))))

password_list=[]

for char in range(0,nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(password)

    

