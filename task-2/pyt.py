import pytesseract
from PIL import Image

img = Image.open('image1.png')

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
l=[]
g=[]

text = pytesseract.image_to_string(img)
for i in text:
	l.append(i)
print(l)
g.append(l[0])
g.append(l[2])
print(int(g[0])+int(g[1]))
