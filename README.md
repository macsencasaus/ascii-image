# ascii image creator

This script generates an ascii represenation of an image!

## Getting Started

Run the following to install the requirements, ideally in a fresh virutal environment

```
pip install -r requirements.txt
```

Add the images you would like to convert to the `./img` directory. 100x100 resolution images work best.

Then run the following to generate `.txt` files for each image in the `./output` directory.

```
python ascii_image.py
```

Checkout the samples previously generated!

## More

The `font_area.py` is what creates the dictionary that translates a given greyscale value [0,1] to a corresponding ascii value. It essentially draws each ascii character on a 20x20 array and takes the mean of each one.

Running it prints the entire dictionary:
```
python font_area.py
```