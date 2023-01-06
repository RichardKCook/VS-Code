numbers = [1,2,3]

diff_numbers=[4,5,6]

new_numbers = [numbers[number] + diff_numbers[number] for number in range(len(numbers))]

print(new_numbers)


numbers = [1,2,3]

new_numbers = [number + 1 for number in numbers]

print(new_numbers)


name = "Richard"

new_list = [letter for letter in name]

print(new_list)



doubled_range = [i*2 for i in range(1,5)]

print(doubled_range)



first_list = [1,2,3]

second_list = [1,2,3,4,5,6,7,8,9,10]

third_list = [num for num in second_list if num not in first_list]

print(third_list)


names = ["Alex","Beth","Caroline","Dave", "Eleanor","Freddie"]

cap_names = [name.upper() for name in names if len(name) > 5]

print(cap_names)