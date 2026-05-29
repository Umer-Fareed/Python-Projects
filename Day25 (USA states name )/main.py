#with open("weather_data.csv") as data_file:
#   data = data_file.readline()
#  print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"]

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(round(data["temp"].max()))


#data in rows
# print(data[data.day  == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
#
# create a dataframe
# data_dict = {
#     "students" : ["any","james","angela"],
#     "score" : [12,32,43]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
# import pandas
# data = pandas.read_csv("squirrel_count.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "fur color" : ["gray" , "cinnamon", "black"],
#     "count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
#
# }
# df = pandas.DataFrame(data_dict)
# print(df)
# df.to_csv("squirrel_count_by_color.csv")


import turtle
import pandas


screen = turtle.Screen()
screen.title("U. S. State Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/Guess the state" ,
                                    prompt=" What's another state's name?").title()
    if answer_state == "Exit":
        missing_states= [state for state in all_states if state not in guessed_states ]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        print(new_data)
        new_data.to_csv("States_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state)

#state_to_learn.csv








