from PIL import Image, ImageColor, ImageDraw, ImageFont

# Loading input image
img = Image.open('input.jpg')

# Resizing image to max size allowed
size_max = (1280, 720)  # example maximum size
img.thumbnail(size_max)

# Creating new image with solid background color
bkg_color = ImageColor.getrgb('#000000')
thumbnail = Image.new('RGB', size_max, bkg_color)

# Creating a semi-transparent overlay using alpha
overlay_color = ImageColor.getrgb('#000000')
overlay = Image.new('RGBA', img.size, overlay_color + (128,))

# Pasting input image onto new background with overlay
img_width, img_height = img.size
thumbnail.paste(img, ((size_max[0]-img_width)//2, (size_max[1]-img_height)//2))
thumbnail.paste(overlay, ((size_max[0]-img_width)//2, (size_max[1]-img_height)//2), mask=overlay)

# Configuring text
text = "My Awesome App"
font = ImageFont.truetype('arial.ttf', 50)  # using local font + font size
text_color = '#fff'  
draw = ImageDraw.Draw(thumbnail)

# Add text to the thumbnail
text_bbox = draw.textbbox(((size_max[0]-img_width)//2, (size_max[1]-img_height)//2), text, font=font)

# Center the text horizontally and vertically in the thumbnail
text_x = (size_max[0] - text_bbox[2]) / 2
text_y = (size_max[1] - text_bbox[3]) / 2
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Save the thumbnail image
thumbnail.save('result.jpg')