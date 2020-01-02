from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

img=Image.open('image.jpg')
text=pytesseract.image_to_string(img)
img.show()

print(text)
