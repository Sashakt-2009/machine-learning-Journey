# Image Lab

A small image processing demo that generates a random RGB image, computes image statistics, applies color filters, crops, flips, and changes brightness.

## Contents

- `Imagelab.py` - main script that creates a random image and saves several processed versions.
- `utils.py` - helper functions for cropping, brightness adjustment, negative conversion, and black-and-white conversion.
- `Saves/` - output folder where generated images are stored.

## Features

- Generate a random 600×600 RGB image.
- Print array and image statistics:
  - shape
  - dimensions
  - data type
  - number of elements
  - mean brightness
  - max/min pixel values
  - brightness standard deviation
- Save the original image to `Saves/img.png`.
- Create and save single-channel versions:
  - red-only
  - green-only
  - blue-only
- Crop the image using `utils.Crop()`.
- Flip the image vertically and horizontally.
- Increase image brightness using `utils.change_brightness()`.

## Requirements

- Python 3.x
- NumPy
- Pillow

Install dependencies with:

```bash
pip install numpy pillow
```

## Usage

Run the script from the `image lab` folder or by specifying the path:

```bash
cd "c:\Users\gdlga\OneDrive\Desktop\machine learning\image lab"
python Imagelab.py
```

Generated output images are saved in the `Saves/` directory.

## Notes

- `utils.py` also includes `negative_img()` and `black_white()` functions that are available for additional image transformations.
- The current script uses random pixel data, so each run produces a unique image.
