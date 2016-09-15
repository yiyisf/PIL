
from PIL import Image
import glob, os


im = Image.open("image/001.jpg")

print(im.format, im.size, im.mode)

im.rotate(180).show()  #向右旋转角度
