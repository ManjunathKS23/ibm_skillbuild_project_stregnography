import pytesseract
from PIL import Image

# Path to the Tesseract OCR executable (change it if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  

# Load the image
image_path = "C:\web\hero.png"
image = Image.open(image_path)

# Convert the image to grayscale for better OCR results
image = image.convert("L")

# Process the image and extract text
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
