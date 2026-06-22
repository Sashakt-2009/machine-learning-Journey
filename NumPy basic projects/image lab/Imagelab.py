import numpy as np
from PIL import Image

arr = np.random.randint(0, 256, (600, 600, 3), dtype=np.uint8)

img = Image.fromarray(arr)

print(f"shape: {arr.shape}\n no. of dimensions: {arr.ndim}\n dtypes: {arr.dtype}\n no. of elements: {arr.size}")