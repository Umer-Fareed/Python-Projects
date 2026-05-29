#FilenotFound

# try:
#     file= open("a_file.txt")
#     a_dict = { "key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file= open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key { error_message} does not exist ")
# else:
#     content= file.read()
#     print(content)
# finally:
#



#key error
# a_dict= {"key":"value"}
# value = a_dict["non_existent_key"]

#IndexError
# fruit_list= ["apple", "banana", "pear"]
# fruit= fruit_list[3]

#TypeError
# text= "abc"
# print(text + 5)


#Exersice 1
# fruits= ["apple", "pear", "orange"]
#
# def make_pie(index):
#     try:
#         fruit= fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

#Exersice 2
# facebook_posts= [
#     {'likes':21, 'comments':2},
#     {'likes':21, 'comments':2, 'share':1},
#     {'likes':21, 'comments':2, 'share':3},
#     {'share':21, 'comments':2},
#     {'share':21, 'comments':2},
#     {'likes':21, 'comments':2}
#
#
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['likes']
#     except KeyError:
#         pass
#
# print(total_likes)


