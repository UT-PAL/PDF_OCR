#OCR Text Underlining and PDF Conversion
##Overview
This Python script performs Optical Character Recognition (OCR) on a given PDF file using the EasyOCR library. It searches for specific text (provided by the user) in the document and highlights (underlines) the found text with a randomly chosen color. The results are saved as images and then converted back into a PDF.

##Features:
Converts PDF pages into images using the pdf2image library.

Performs OCR to detect and read text using EasyOCR.

Underlines matched text with a randomly selected color.

Saves the images with underlined text as PNG files.

Converts the images back into a PDF document using img2pdf.

##Requirements
Before running the script, you need to install the following dependencies:

easyocr: For OCR text recognition.

Install: pip install easyocr

numpy: For handling arrays.

Install: pip install numpy

pdf2image: For converting PDF pages to images.

Install: pip install pdf2image

Pillow (PIL): For image manipulation.

Install: pip install Pillow

opencv-python: For handling image processing.

Install: pip install opencv-python

img2pdf: For converting images back into PDF.

Install: pip install img2pdf

random: For selecting random colors.

re: For text normalization (used to compare text).

How It Works
Step 1: Convert PDF to Images
The script uses the pdf2image library to convert each page of the input PDF file into an image (at 300 DPI resolution).

Step 2: OCR and Text Matching
EasyOCR is used to perform OCR on each image to detect text. The script checks if the given old_text (search text) exists in the recognized text. It normalizes the text for case-insensitive comparison.

Step 3: Underline Matched Text
Once a match is found, the script draws a colored underline (a rectangle below the matching text) on the image. The underline color is randomly chosen from a predefined set.

Step 4: Save and Convert to PDF
After processing all pages, the images with underlined text are saved as PNG files. These images are then converted back into a single PDF using the img2pdf library.

Step 5: Output PDF
The final output is a PDF document with the matched text underlined.

Usage
Running the Script
Place the PDF file you want to process in the same directory as the script or specify the full path to the file.

Update the call to easy_ocr() with the path to your PDF and the text you want to find and underline.

python
Copy
Edit
easy_ocr("path_to_your_pdf.pdf", "text_to_search_for")
Replace "path_to_your_pdf.pdf" with the path to your PDF, and "text_to_search_for" with the text you'd like to find and underline.

Example:
python
Copy
Edit
easy_ocr("utpal.pdf", "django")
This will process the utpal.pdf file and underline the word "django" wherever it appears.

Output:
The processed PDF will be saved as output_ocr.pdf.

Intermediate images will be saved as underlined_text1.png, underlined_text2.png, etc., in the same directory.

Notes:
The OCR is case-insensitive.

You can modify the script to adjust the underline position or customize the colors.

The script randomly selects colors from a predefined list for underlining.

If the script fails to find the old_text, it will not underline anything.

Troubleshooting
Missing Dependencies: Ensure all required libraries are installed.

OCR Accuracy: OCR quality depends on the PDF's text quality and resolution. Ensure the PDF is clear and readable for better results.

Image Size/Resolution: The script converts the PDF pages to images at 300 DPI. If the images are too large, you can adjust the DPI for faster processing, but this may affect OCR accuracy.

License
This project is licensed under the MIT License - see the LICENSE file for details.
