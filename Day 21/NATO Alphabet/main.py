import pandas

bet = pandas.read_csv(
    "/Users/Cook/Documents/VS Code/Day 21/NATO Alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for index,row in bet.iterrows()}


name = input("What's your name?: ").upper()

conv = [nato_dict[letter] for letter in name]

print(conv)