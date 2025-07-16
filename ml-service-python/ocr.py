from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import os


def test_noisy_image():
    # Optional: Set the Tesseract command path on Windows
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load the image
    img_path = './test/Noisy.jpg'
    if not os.path.exists(img_path):
        print("Image file not found!")
    else:

        # Load an image with noise or low contrast
        img = Image.open('./test/Noisy.jpg')

        # Convert the image to grayscale
        img = img.convert('L')

        # Apply a median filter to reduce noise
        img = img.filter(ImageFilter.MedianFilter())

        # Enhance the image contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        # Extract text from the pre-processed image
        text = pytesseract.image_to_string(img)

        print(text)


def extract_text(img):

    # Convert the image to grayscale
    img = img.convert('L')

    # Apply a median filter to reduce noise
    img = img.filter(ImageFilter.MedianFilter())

    # Enhance the image contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    # Extract text from the pre-processed image
    text = pytesseract.image_to_string(img)

    return text
