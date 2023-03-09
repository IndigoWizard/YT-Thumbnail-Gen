from PIL import Image, ImageColor, ImageDraw, ImageFont

# Loading input image
img = Image.open('input.jpg')

# Resizing image to max size allowed
size_max = (1280, 720)  # example maximum size
img.thumbnail(size_max)

# Creating new image with solid background color
bkg_color = ImageColor.getrgb('#000000')
thumbnail = Image.new('RGB', size_max, bkg_color)

# Creating a semi-transparent overlay
overlay_color = ImageColor.getrgb('#000000')
overlay = Image.new('RGBA', img.size, overlay_color + (128,))

# Pasting input image onto new background with overlay
img_width, img_height = img.size
thumbnail.paste(img, ((size_max[0]-img_width)//2, (size_max[1]-img_height)//2))
thumbnail.paste(overlay, ((size_max[0]-img_width)//2, (size_max[1]-img_height)//2), mask=overlay)