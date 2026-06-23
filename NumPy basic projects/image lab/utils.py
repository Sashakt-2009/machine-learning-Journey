import numpy as np 
from PIL import Image

def Crop(Y_dims: tuple[int, int], X_dims: tuple[int, int], image: Image):   # Y_dims = (start_pixel,end_pixel) in Y axis, X_dimensions = (start_pixel,end_pixel) in X axis)
    img_view = np.array(image,dtype=np.uint8)                               # convert PIL.IMAGE.IMAGE  --> np.array
    croped_view = img_view[Y_dims[0]:Y_dims[1], X_dims[0]:X_dims[1]]        # cropping the array using slicing
    croped_img = Image.fromarray(croped_view)                           
    return croped_img                                                       # retuning back the cropped image
