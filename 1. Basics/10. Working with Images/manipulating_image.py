#!/usr/bin/env python3

# Load and show an image with Pillow
from PIL import Image

# Load the image
img = Image.open('Images/2/Image_20.jpg').convert("L")  # Grayscale

newImage = img.resize((1280, 720))  # Resizing the image

# Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

# Show Image
# img.show()
newImage.rotate(45).show()

# Save image
# img.save('Images/1/Image_11_grayscale.jpg')
newImage.save('Images/2/Image_20.png')
