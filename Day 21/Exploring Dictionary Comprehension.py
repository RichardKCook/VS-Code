from random import randint
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: randint(0, 100) for student in names}


passed_students = {student: score for student,
                   score in student_scores.items() if score >= 70}

print(passed_students)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words  = sentence.split()

result = {word:len(word) for word in words}


print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:float("{:.1f}".format(temp*(1.8)+32)) for day,temp in weather_c.items()}


print(weather_f)




student_data_frame = pandas.DataFrame(names)

print(student_data_frame)

#Loop thru data frame

for (key,value) in student_data_frame.items():
    print(value)

for (index, row) in student_data_frame.iterrows():
    print(row)