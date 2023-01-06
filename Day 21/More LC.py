numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


squared_numbers = [i**2 for i in numbers]


print(squared_numbers)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [i for i in numbers if i%2 == 0]

print(result)




with open("/Users/Cook/Documents/VS Code/Day 21/file1.txt") as one:

    file1 = one.readlines()

with open("/Users/Cook/Documents/VS Code/Day 21/file2.txt") as two:

    file2 = two.readlines()

stripped_one = []
stripped_two = []

for line in file1:
    stripped_one.append(int(line.strip()))

for line in file2:
    stripped_two.append(int(line.strip()))

result = [i for i in stripped_one if i in stripped_two]


print(result)
