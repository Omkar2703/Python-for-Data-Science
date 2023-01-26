#Calculating Minimum and Maximum among array
import numpy as np

horsepower = np.array([100, 102, 115, 108, 95, 76])

#First let us find min and max
print("Minimum: ", np.min(horsepower))
print("Maximum: ", np.max(horsepower))
# Output
# Minimum:  76
# Maximum:  115

#Now let us find index number of Max and min number
print("Minimum number present at index: ", np.argmin(horsepower))
print("Maximum number present at index: ", np.argmax(horsepower))
# Output
# Minimum number present at index:  5
# Maximum number present at index:  2