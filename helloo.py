import numpy as np

eye_array = np.eye(4, k  = 1, dtype = int)
eye_array[eye_array == 0] = 7
eye_array[eye_array < 7] = 9
eye_array[1:3,1:3] = 3
eye_array[3,3] = 500
print(eye_array)
