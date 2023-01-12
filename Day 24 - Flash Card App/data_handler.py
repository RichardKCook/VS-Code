import pandas
import random
data = pandas.read_csv(
            "/Users/Cook/Documents/VS Code/Day 24 - Flash Card App/data/french_words.csv")
global words
words = {row.French:row.English for index,row in data.iterrows()}

class Data_Handler:
    def __init__(self):
        
        
        self.dict = data.to_dict(orient="records")
        

    def get_words(self):
        pairs = words.items()
        french = [key for key,value in pairs]
        english = [value for key,value in pairs]
        index = random.randint(0,len(french))
        french_word = french[index]
        english_word = english[index]

        pair = french_word,english_word

        return pair

    def words_to_learn(self, known_word):
        
        try:
         del words[known_word]
        
        except KeyError:
            pass

        file = pandas.DataFrame(words,index=[0])

        file.to_csv("French Words to Learn.csv",index=False)
       
        