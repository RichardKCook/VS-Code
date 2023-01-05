import csv
import pandas


# with open("/Users/Cook/Documents/VS Code/Day 20/CSV/weather_data.csv") as f:
#     data = csv.reader(f)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

data = pandas.read_csv(
    "/Users/Cook/Documents/VS Code/Day 20/CSV/weather_data.csv")

print(type(data))
print(type(data["temp"]))

dict = data.to_dict()
print(dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(sum(temp_list)/len(temp_list))  # average

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)

print(data[data.day == "Monday"]) #get monday row

print(data[data.temp == data.temp.max()]) #get max temp row

monday = data[data.day == "Monday"]

monday_temp = int(monday.temp)
 # type: ignore
conv_f = monday_temp * (9/5) + 32

print(conv_f)


data_dict = {
    "students": ["jim", "mike", "tom"],
    "scores": [76, 56, 65]
}

my_list = pandas.DataFrame(data_dict)

my_list.to_csv("new_csv.csv")
