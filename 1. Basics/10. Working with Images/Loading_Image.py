#!/usr/bin/env python3

# Load and show an image with Pillow
from PIL import Image

# Load the image
img = Image.open('Images/1/Image_11.jpg')

# Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

# Show Image
img.show()
