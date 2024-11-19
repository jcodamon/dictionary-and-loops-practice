# # Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# # print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[0]['Combo,Name'])
# print(students[0]['Email'][0])
# print(students[0]['Email'][1])

# # for loops allow us to
# #iterate through the data
# #and perform some function

# #we are iterating through the data
# #and printing the name and email of the students
# #we are also printing a line of underscores to separate the students
# #we are also printing a line of underscores to separate the students
# # for student in students:
# #     print(student['Combo,Name'])
# #     print(student['Email'][0])
# #     print(student['Email'][1])
# #     print(student['HR'])
# #     print(student['GL'])
# #     print("_"*25)


# # we are asking the user to input their name
# # then we are checking if the name is in the data
# # if the name is in the data we are printing the name and "this works"
# # CPSID = int(input("what is you ID?")) 
# # for student in students:
# #     if CPSID == student['CPSID']:
# #         print(student['CPSID'])
# #         print("this works")


# # Let's try to print out the emails of the students:    


# #Jesse Codamon, Esteban Alvarez, Cesar Guzman
# #Question 1
# # for student in students:
# #     print(student['Combo,Name'])
# #     print(student['Email'][0])
# #     print(student['Email'][1])
# #     print("-"*25)





# #Question 2
# # HR = (input('What is your HR?: '))

# # for student in students:
# #     if HR == student['HR']:
# #         print(student['Combo,Name'])
# #         print(student['Email'][0])
# #         print(student['Email'][1])
# #     else:
# #         print('No students found in this homeroom.')
# #     break





# #Question 3
# # name = (input('What is your name first name?: '))

# # for student in students:
# #     if name == student['FName']:
# #         print(student['FName'])
# #         print(student['HR'])




# #Question 4
# # for student in students:
# #     if student['GL'] == 10:
# #         print(student['Combo,Name'])
# #         print(student['CPSID'])
# #         print('-'* 25)
# #     else:
# #         print('No students in grade level.')



# #Question 5
# # for student in students:
# #     print(student['Email'][0], student['Email'][1],",")



# #Question 6
# # last_name = students['LName']
# # for student in students:
# #     if last_name == student['LName']:
# #         print(student['LName'])

# #Question 7

# homeroom = input("What's your homeroom?: ")

# for student in homeroom:
#     if student['HR'] == homeroom:
#         print(students['Combo,Name'])
#         print(students['HR'])
#         print('-'* 25)
#     else:
#         print('No students in homeroom.')
#         break






# Example: Updating a student's first name in a list of student dictionaries
for student in students:
    if student['CPSID'] == 10000012:  # Replace with the condition to find the specific student
        student['FName'] = 'Lilly'  # Update the first name
        student['LName'] = 'Barocio'   # Update the last name
        print(f"Updated student: {student}")

# Delete a specific key-value pair in a dictionary:
for student in students:
    if student['CPSID'] == 10000013:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        print(f"Updated student: {student}")

# # Delete an entire object from the list:
# Using a loop to find and remove a student by a specific condition
students = [student for student in students if student['CPSID'] != 10000014]  # Keeps all except the one with CPSID 123456


# Update a specific entry by index
students[2]['FName'] = 'Lilly'  # Updates the first student's first name
students[2]['LName'] = 'Barocio'
print(students[0])

# Direct Access for Known Index
# If you know the index of the item you want to modify:
# Update a specific entry by index
students[0]['FName'] = 'manny'  # Updates the first student's first name
students[0]['LName'] = 'salgado'
print(students[0])

# # Remove a specific student by index
# del students[0]  # Removes the first student in the list

# Adding New Key-Value Pairs to Existing Objects
# To add a new piece of information (e.g., a new contact number) to each student:
# Example: Add a 'ContactNumber' field to each student
# for student in students:
#     student['ContactNumber'] = '708-304-8926'  # Assign a default or specific value

# Inserting a New Object into the List
# To add a completely new student record to the dataset:
# Create a new student dictionary
new_student = {
    'CPSID': 10000012,
    'Combo,Name': 'Doe, John',
    'FName': 'John',
    'LName': 'Doe',
    'MName': 'Paul',
    'HR': 'B220',
    'GL': 11,
    'Email': ['john.doe@example.com', 'j.doe@example.org']
}
# Add the new student to the list
students.append(new_student)


print("New student added:")
print(new_student)



# Overwrite the `student_data.py` file with the updated data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        f.write(f"    {repr(student)},\n")  # Use repr() to write the dictionary as a string suitable for Python code
    f.write("]\n")






