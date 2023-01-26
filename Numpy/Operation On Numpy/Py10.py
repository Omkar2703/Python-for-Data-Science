#Students marks in 4 subjects
import numpy as np
students_marks = np.array([[67, 45],[90, 92],[66, 72],[32, 40]])
#Broadcasting
students_marks += [5,10]
print(students_marks)
