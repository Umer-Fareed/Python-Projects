# programming_dictionary = {
#     "bug" : " an error",
#     "function": "repeatable code"
# }
# #retrive and item from the dictionary
# print(programming_dictionary["bug"])
#
# #addinn in dictionary
# programming_dictionary["loop"] = " looping for code "
# print(programming_dictionary)
#
# #empty dictionary
# empty_dictionary = {}

# #wipe dictionary
# # programming_dictionary ={}
#
#
# #edit an item in a dictionary
# programming_dictionary["bug"] = " a moth in your computer "
#
#
# #loop through a dictionary
# for key in programming_dictionary:
#     print(key )
#     print(programming_dictionary[key])
from seaborn.utils import ci_to_errsize

#grading program
student_score = {
    "harry": 81,
    "umar" : 33,
    "adeel": 76,
    "maan" : 65
}

#studend grades
# student_grades = {}
#
# #assign grade
# for students in student_score:
#     score = student_score[students]
#     if score > 90:
#         student_grades[students] = "outstanding"
#     elif score > 80:
#         student_grades[students] = "Exceeds expectations"
#     elif score > 70:
#         student_grades[students] = "acceptable"
#     else:
#         student_grades[students] = "fail"
#
# print(student_grades)

#nesting
# capitals = {
#     "france " : " paris" ,
#     "germany" : " berlin"
#
# }
# #nesting a list in dictionary
# travel_log = {
#     "france " :{"cities_visited": [ "paris", "lille", "dijon"],
#                 "total_visit" : 21},
#     "germany" :{"cities_visited": ["berlin", "hamburg" "stuttgart"],
#                 "total_visit" : 54}
# }


#write a function to add new element of the list
def add_new_country(country,number_visited,cities):
    new_country = {}
    new_country["country"] = country
    new_country["total_visit"] = number_visited
    new_country["cities_visited"] = cities
    travel_log.append(new_country)
# #nesting dictionary in a list
travel_log = [
        {"country " :"france ",
         "cities_visited": [ "paris", "lille", "dijon"],
         "total_visit" : 21
         },
        {
            "country" :"germany",
         "cities_visited": ["berlin", "hamburg" "stuttgart"],
         "total_visit" : 54
        }
]
print(travel_log)


