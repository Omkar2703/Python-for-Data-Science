#creating a list of Marks
import numpy as np
Marks = [100, 140, 180, 220, 260, 300]
#creating a numpy array from Marks list
Marks_arr = np.array(Marks)
#creating filter array
filter_arr = Marks_arr > 160
newarr = Marks_arr[filter_arr]
print(filter_arr)
print(newarr)
