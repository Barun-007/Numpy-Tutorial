import numpy as np

# 2D array:

from_list = np.array([[1,2,3,4,5]])
print(from_list)
print(type(from_list[0,0]))

from_list = np.array([[1,2,3,4], [5,6,7,8]])
print(from_list)
print(type(from_list[0][1]))

my_arr = np.array((np.arange(1,8,2), np.arange(0,8,2)))
print(my_arr)
print(my_arr[1][3])
print("2D array shape:", my_arr.shape)

arr_2D = my_arr.reshape((2,2,2))
print(arr_2D)
print(my_arr)


# copy the Array:

my_view = my_arr.view()
my_copy = my_arr.copy()
my_copy[:] = 8

print("\nits copy method():\n")
print(my_copy) # it copy the array without touching the original array
print(my_arr)  # my_arr will remain the same

print("\nNow its view method():\n")
my_view[:] = 7
print(my_view) # it change the original array also
print(my_arr) # Here Original array is changed

