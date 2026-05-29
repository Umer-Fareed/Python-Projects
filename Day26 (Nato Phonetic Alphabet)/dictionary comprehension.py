#Dictionary Comprehension
#new_dict= {new_key:new_value for (key,value) in dict.item() if item}
# import random
# names= ["umar" , "adeel", "haroon", "maan", "sayam"]
# # student_Score= {
# #     "umar": 64,
# #     "adeel": 89,
# #     "haroon": 87,
# #     "maan": 98,
# #     "sayyam": 67
# # }
# students_score= {student:random.randint(1,100) for student in names}
# print(students_score)
#
# passed_students= {student:score for(student,score) in students_score.items() if score >= 40}
# print(passed_students)


#2 exercise
# sentence= "What is the Airspeed velocity of ann unladen Swallow"
#
# new_dict= {words:len(words) for words in sentence.split()  }
# print(new_dict)

#3 exercise
weather_c= {
    "monday":12,
    "tuesday":14,
    "wednesday":15,
    "thursday":14,
    "friday":21,
    "saturday":22,
    "sunday":24
}
temp_in_f= {day:temp*9/5+32 for (day,temp) in weather_c.items()}
print(temp_in_f)

#iteration in dataframes
# import pandas
# student_data= {
#     "students": ["fareed", "umar","adeel","haroon"],
#     "score": [32,43,5,64]
# }
#
# student_data_frame= pandas.DataFrame(student_data)
# print(student_data_frame)
# for (index,row) in student_data_frame.iterrows():
#     print(row.score)