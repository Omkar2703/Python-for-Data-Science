#Slicing array
import numpy as np
#Slicing 1D array
# students = np.array(['Omkar', 'Ramchandra', 'Jayashri', 'Harshada', 'Patil'])
# print(students[1:3])
#Output
#['Ramchandra' 'Jayashri']

#Slicing 2D array
students = ['Omkar', 'Deep', 'Pranav', 'Sukant']
roll_id = [100, 101, 102, 103]
user_name = np.array([students, roll_id])
print(user_name)
print(user_name[0:3, 0:3])
#Slicing First three names
# Output after slicing
# [['Omkar' 'Deep' 'Pranav']
#  ['100' '101' '102']] 