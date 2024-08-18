import numpy as np

eye_array = np.eye(4, k=1)
''' its creates a Indentity Matrix with (4 x 4) '''

eye_array[eye_array == 0] = 2
eye_array[eye_array < 2] = 9
# Row Select:
eye_array[0] = 3 # entire First row will be select and all elements assign to 3.
eye_array[:2] = 9 # First two rows are selected .. 0th and 1st
eye_array[2:] = 2 # last two rows will be selected .. 2nd and 3rd
''' row and column count starting with 0 '''

# Column Select:
eye_array[:, 0] = 7 # To select 1st Column.
eye_array[:, -1] = 5 # To select Last column.
eye_array[1:3, 1:3] = 8
eye_array[2:, :2] = 9
print("Original array:")
print( eye_array)

# Sorting an Array: by default row sorted 
sorted_array = np.sort(eye_array) # By default its sorted by rows
print("Row wise Sorted array:")
print(sorted_array)

''' 
If I want to sort the column then this:
'''
sorted_array = np.sort(eye_array, axis = 0, kind= "quicksort") #  its sorted by column. axis = 0 means column
print("Colummn wise Sorted array:")
print( sorted_array)

