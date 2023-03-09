from PIL import Image, ImageColor, ImageDraw, ImageFont

# Loading input image
img = Image.open('input.jpg')

# Resizing image to max size allowed
size_max = (1280, 720)  # example maximum size
img.thumbnail(size_max)
