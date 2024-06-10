# Given the names and grades for each student in a class of  students, store them in a nested list and 
# print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

list = [['Charlie', 70.65], ['Alice', 12.44], ['David', 89.33], ['Bob', 7.98], ['Frank', 48.21]]

data_dict = {}
for item in list:
    name, mark = item
    data_dict["name"].append(name)
    data_dict["mark".append(mark)]

print(data_dict)
