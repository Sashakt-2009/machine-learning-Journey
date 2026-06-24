import numpy as np 
from PIL import Image

def Crop(Y_dims: tuple[int, int], X_dims: tuple[int, int], image: Image):   # Y_dims = (start_pixel,end_pixel) in Y axis, X_dimensions = (start_pixel,end_pixel) in X axis)
    img_view = np.array(image,dtype=np.uint8)                               # convert PIL.IMAGE.IMAGE  --> np.array
    croped_view = img_view[Y_dims[0]:Y_dims[1], X_dims[0]:X_dims[1]]        # cropping the array using slicing
    croped_img = Image.fromarray(croped_view)                           
    return croped_img                                                       # retuning back the cropped image

def change_brightness(image, value):

    arr = np.array(image,dtype=np.uint8)        

    R_vals = arr[:, :, 0].copy()        
    G_vals = arr[:, :, 1].copy()
    B_vals = arr[:, :, 2].copy()


    brightness = (0.299 * R_vals) + (0.587 * G_vals) + (0.114 * B_vals)

    increased_brightness = brightness + value

    R = increased_brightness*0.299

    R_vals = np.clip((R_vals + (increased_brightness/0.299)),0, 255).astype(np.uint8)
    G_vals = np.clip(G_vals + (increased_brightness/0.587),0,255).astype(np.uint8)
    B_vals = np.clip((B_vals +  (increased_brightness/0.114)),0,255).astype(np.uint8)

    arr[:, :, 0] = R_vals
    arr[:, :, 1] = G_vals
    arr[:, :, 2] = B_vals
    img = Image.fromarray(arr)
    return img

def negative_img(image):
    arr = np.array(image,dtype=np.uint8)
    negative_img = np.absolute(255-arr)
    return Image.fromarray(negative_img)

def black_white(image):
    arr = np.array(image, dtype=np.uint8)
    arr[arr>= 128] = 255
    arr[arr<128] = 0
    return Image.fromarray(arr)
