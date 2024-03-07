from PIL import Image, ImageDraw

# Load the image
# image_path = 'path_to_your_image.jpg'
image_path = "/Users/bhartiprakash/Documents/Santa Clara/Courses/Quarter 6/DiretedReaserch/ScavengerHunt/one.jpg"
img = Image.open(image_path)

# Prepare to draw on the image
draw = ImageDraw.Draw(img)
width, height = img.size

# Draw a grid
for x in range(0, width, 1):  # Change '1' to increase grid cell size
    draw.line((x, 0, x, height), fill='gray', width=0)
for y in range(0, height, 1):  # Change '1' to increase grid cell size
    draw.line((0, y, width, y), fill='gray', width=0)

# Save or display the image
img.show()  # Or img.save('path_to_save_image_with_grid.jpg')