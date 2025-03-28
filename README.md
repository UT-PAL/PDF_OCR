# OCR Text Underlining and PDF Conversion

## Overview

This Python script performs Optical Character Recognition (OCR) on a given PDF file using the EasyOCR library. It searches for a specified text (provided by the user) in the document and highlights (underlines) the found text with a randomly chosen color. The results are saved as images, and these images are then converted back into a PDF.

### Features:
- Convert PDF pages into images using the `pdf2image` library.
- Perform OCR to detect and read text using EasyOCR.
- Underline matched text with a randomly selected color.
- Save images with underlined text as PNG files.
- Convert the images back into a single PDF using `img2pdf`.

## Requirements

Before running the script, you need to install the following dependencies:

1. **easyocr**: For OCR text recognition.
   - Install: `pip install easyocr`
2. **numpy**: For handling arrays.
   - Install: `pip install numpy`
3. **pdf2image**: For converting PDF pages to images.
   - Install: `pip install pdf2image`
4. **Pillow (PIL)**: For image manipulation.
   - Install: `pip install Pillow`
5. **opencv-python**: For handling image processing.
   - Install: `pip install opencv-python`
6. **img2pdf**: For converting images back into PDF.
   - Install: `pip install img2pdf`
7. **random**: For selecting random colors.
8. **re**: For text normalization (used to compare text).

## How It Works

### Step 1: Convert PDF to Images
The script uses the `pdf2image` library to convert each page of the input PDF file into an image. The pages are converted at a resolution of 300 DPI for better accuracy.

### Step 2: OCR and Text Matching
The EasyOCR library is used to perform OCR on each image to detect text. The script then compares the detected text with the specified `old_text` (text to search for) by normalizing both texts for case-insensitive matching.

### Step 3: Underline Matched Text
Once a match is found, the script draws a colored underline (a rectangle below the matching text) on the image. The underline color is randomly chosen from a predefined list.

### Step 4: Save and Convert to PDF
After processing all pages, the images with underlined text are saved as PNG files. These images are then converted back into a single PDF document using the `img2pdf` library.

### Step 5: Output PDF
The final output is a PDF document containing the matched text underlined, which is saved as `output_ocr.pdf`.

## Usage

### Running the Script

1. Place the PDF file you want to process in the same directory as the script or specify the full path to the file.
2. Update the `easy_ocr()` function call with the path to your PDF and the text you want to search for and underline.

```python
easy_ocr("path_to_your_pdf.pdf", "text_to_search_for")


Example:
python
Copy
Edit
easy_ocr("utpal.pdf", "django")
This will process the utpal.pdf file and underline the word "django" wherever it appears in the document.

Output:
The processed images will be saved as underlined_text1.png, underlined_text2.png, etc., in the same directory.

The final output PDF will be saved as output_ocr.pdf.

Notes:
The OCR is case-insensitive and performs a normalized comparison.

The underline color is randomly chosen from a predefined list.

The script processes each page in the PDF and saves images of the underlined text for each page.

Troubleshooting
Missing Dependencies: Ensure all required libraries are installed. Use pip install -r requirements.txt if you have a requirements.txt file with dependencies listed.

OCR Accuracy: The accuracy of the OCR depends on the quality of the PDF and the text resolution. Ensure that the PDF is clear for better OCR results.

Performance: The script processes the PDF at 300 DPI, which ensures high-quality results but can be resource-intensive for large documents. You can adjust the DPI for faster processing if needed.

License
This project is licensed under the MIT License - see the LICENSE file for details.
