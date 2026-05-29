#old method
# numbers= [1,2,3]
# new_list = []
# for n in numbers:
#     add_1= n+1
#     new_list.append(add_1)
# print(new_list)
#
# #list comprehension
# new_lists= [n+1 for n in numbers]
# print(new_lists)
#
# #2
# name= "Angela"
# name_list= [ letter for letter in name]
# print(name_list)
#
# #3
# new_range= [n*2 for n in range(1,5)]
# print(new_range)
#
# #condition in list comprehension
# #new_list = [new_item for item in list if text]
#
# names= ["umar" , "adeel", "haroon", "maan", "sayam"]
# print(names)
# short_names= [name for name in names if len(name) < 5]
# print(short_names)
#
# long_Name= [name.upper() for n in names if len(names)>5]
# print(long_Name)

#4
# numbers= [1,1,2,3,5,8,13,21,34,55]
# new_num= [n*n for n in numbers]
# print(new_num)

#5
# numbers= [1,1,2,3,5,8,13,21,34,55]
# even_list= [n for n in numbers if n%2==0]
# print(even_list)

#6
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file1:
#     file_2_data = file1.readlines()
# result= [int(num)for num in file_1_data if num in file_2_data]
# print(result)