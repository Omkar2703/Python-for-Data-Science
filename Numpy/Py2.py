#Creating 2D array

import numpy as np


car_name = ['Ertiga', 'Fortuner', 'Nexon', 'Hector', 'Scorpio', 'Endeveour']

horse_power = [300, 600, 150, 400, 200, 900]

Cars = np.array([car_name, horse_power])
print(Cars)

# Output
# [['Ertiga' 'Fortuner' 'Nexon' 'Hector' 'Scorpio' 'Endeveour']
#  ['300' '600' '150' '400' '200' '900']]
