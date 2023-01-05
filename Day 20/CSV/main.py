import pandas


data = pandas.read_csv(
    "/Users/Cook/Documents/VS Code/Day 20/CSV/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_rows = data[data["Primary Fur Color"] == "Gray"]
cinnamon_rows = data[data["Primary Fur Color"] == "Cinnamon"]
black_rows = data[data["Primary Fur Color"] == "Black"]

count_gray = len(gray_rows)
count_cinnamon = len(cinnamon_rows)
count_black = len(black_rows)

# gray_fur = gray_rows["Primary Fur Color"].to_dict()
# cinnamon_fur = cinnamon_rows["Primary Fur Color"].to_dict()


data_dict = {

    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
 
}


frame = pandas.DataFrame(data_dict)

frame.to_csv("squirrel count.csv")