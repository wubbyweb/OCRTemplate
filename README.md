# OCRTemplate
Template program for OCR processing using tesseract

## Tesseract OCR
Install Tesseract on your system. You can download it from its GitHub repository or use package managers like brew for macOS or apt for Ubuntu.
Python Packages: Install the necessary Python packages using pip:

pip install pytesseract pillow

- Importing Libraries: The script imports the Image module from the PIL (Pillow) library for image processing and pytesseract for OCR.
- Tesseract Path: If Tesseract is not in your system's PATH, specify the full path to the Tesseract executable using pytesseract.pytesseract.tesseract_cmd.
- Function Definition: The function extract_text_from_image takes an image file path as input, opens the image, and uses pytesseract.image_to_string() to extract text from the image.
- Example Usage: The script demonstrates how to call the function with an image path and print the extracted text.

  
This implementation provides a straightforward way to use Tesseract OCR in Python for text extraction from images. Adjust the image path and Tesseract executable path as needed for your environment.
