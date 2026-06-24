import numpy as np, utils
from PIL import Image


# making an array with random RGB values the dimensions are as follows(Y_dims, X_dims, RGB values)
arr = np.random.randint(0, 256, (600, 600, 3), dtype=np.uint8)

# array Statistics
print("ARRAY STATISTICS:")
print(f"shape: {arr.shape}\nno. of dimensions: {arr.ndim}\ndtypes: {arr.dtype}\nno. of elements: {arr.size}\n")


# comverting the generated array to an img
img = Image.fromarray(arr)
img.save("image lab\saves\img.png")

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


# single color only 
red_only = arr.copy()
red_only[:,:,1] = 0
red_only[:,:,2] = 0             # making G and B values 0
red_only_img = Image.fromarray(red_only)
red_only_img.save("image lab\saves\RedOnlyimg.png")

green_only = arr.copy()
green_only[:,:, 0] = 0
green_only[:,:, 2] = 0           # making R and B values 0
green_only_img = Image.fromarray(green_only)
green_only_img.save("image lab\saves\GeenOnlyimg.png")

blue_only = arr.copy()
blue_only[:,:,0] = 0
blue_only[:,:,1] = 0          # making R and B values 0
blue_only_img = Image.fromarray(blue_only)
blue_only_img.save("image lab\saves\BlueOnlyimg.png")

# cropping using custom function in utils.py 

cropped_img = utils.Crop((0,300), (0,300), img)
cropped_img.save("image lab\saves\cropped_img.png")

# flipping img -> vflip & hflip

V_flipped = np.flip(arr, axis=0)
H_flipped = np.flip(arr, axis=1)

V_flipped_img = Image.fromarray(V_flipped)
V_flipped_img.save("image lab\saves\V_flipped_img.png")
H_flipped_img = Image.fromarray(H_flipped)
H_flipped_img.save("image lab\saves\H_flipped_img.png")

#changing brightness
bright_img = utils.change_brightness(img, 10)
bright_img.save("image lab\saves\Bright_img.png")
