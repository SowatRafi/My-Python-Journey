import glob
import os

from PIL import Image

size = 128, 128

for infile in glob.glob("Images/3/*jpg"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(file + ".thumbnail", "JPEG")
