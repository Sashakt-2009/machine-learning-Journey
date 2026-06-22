import numpy as np
from PIL import Image


# making an array with random RGB values the dimensions are as follows(length, breadth, RGB values)
arr = np.random.randint(0, 256, (600, 600, 3), dtype=np.uint8)

# array Statistics
print("ARRAY STATISTICS:")
print(f"shape: {arr.shape}\nno. of dimensions: {arr.ndim}\ndtypes: {arr.dtype}\nno. of elements: {arr.size}\n")


# comverting the generated array to an img
img = Image.fromarray(arr)
img.show()

# image Statistics
print("IMAGE STATISTICS:") 
R_vals = arr[:, :, 0].copy()        
G_vals = arr[:, :, 1].copy()
B_vals = arr[:, :, 2].copy()


brightness = (0.299 * R_vals) + (0.587 * G_vals) + (0.114 * B_vals)
mean_brightness = brightness.sum()/ brightness.size
devation = brightness - mean_brightness
s_devation = np.square(devation)
s_devation = s_devation.sum()
s_devation = np.sqrt(s_devation/brightness.size)



print(f'''mean_brightness: {mean_brightness}\nmax_pixel_val: {(int(R_vals.max()), int(G_vals.max()), int( B_vals.max()))}
min_pixel_val: {(int(R_vals.min()), int(G_vals.min()), int(B_vals.min()))}\nstandard devation in brightness: {s_devation} ''')