from PIL import Image
import pytesseract

# Define the path to the Tesseract executable
# This is necessary if Tesseract is not in your system's PATH
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Update this path based on your installation

def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)
    return text

# Example usage
image_path = 'path_to_your_image.png'  # Replace with your image path
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:\n", extracted_text)
