import pytesseract
from PIL import Image

# Open the image (ensure that the WebP format is supported by Pillow)
img = Image.open('image3.png')

# Specify the correct path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Correct path to Tesseract executable
l=[]
g=[]
# Extract text from the image
text = pytesseract.image_to_string(img)
for i in text:
	l.append(i)
print(l)
g.append(l[0])
g.append(l[2])
print(int(g[0])+int(g[1]))
