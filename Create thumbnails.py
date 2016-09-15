import glob
import os

from PIL import Image

size = 128, 128

for infile in glob.glob("image/*.jpg"):
    file, ext = os.path.splitext(infile)
    print(file, ext)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", format="BMP")


