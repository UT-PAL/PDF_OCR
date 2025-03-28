import easyocr
import numpy as np
from pdf2image import convert_from_path
from PIL import Image,ImageDraw,ImageFont
import cv2
import img2pdf
import random
import re

def normalize_text(text):
    return re.sub(r'[^\w\s]', '', text)


def easy_ocr(filepath, old_text):
    pages = convert_from_path(filepath, 300)  # Convert PDF to images at 300 DPI
    reader = easyocr.Reader(['en'])  # Initialize EasyOCR reader
    image_files=[]
    j=0
    for i, page in enumerate(pages):
        np_page = np.array(page)  # Convert PIL image to NumPy array
        np_page = cv2.cvtColor(np_page, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR
        draw = ImageDraw.Draw(page)
        results = reader.readtext(np_page)  # Perform OCR
        
        for bbox, text, prob in results:
            text_lower = " ".join(text.lower().split())
            old_text_lower = " ".join(old_text.lower().split())
            
            if normalize_text(old_text_lower) in normalize_text(text_lower):  # If part of the text matches
                print(f"item no: {j} , text:{text_lower}\n")
                x_min = int(min(p[0] for p in bbox))
                y_min = int(min(p[1] for p in bbox))
                x_max = int(max(p[0] for p in bbox))
                y_max = int(max(p[1] for p in bbox))

                # Underline position (slightly below the text)
                underline_y = y_max + 2  # Shift line a few pixels down
                color = ["red",'blue','yellow','green','lightgreen',"black","gray","purple","orange","brown"]
                # Draw underline
                #draw.line([(x_min, underline_y), (x_max, underline_y)], fill=random.choice(color), width=10)
                x_match = text_lower.find(old_text_lower)+2
                draw.rectangle([(x_min+x_match,y_min),(x_max+2,underline_y)],outline=random.choice(color),width=4)
                j+=1
        output_filename = f"underlined_text{i+1}.png"
        page.save(output_filename)
        print(f"Saved output as {output_filename}")
        # Convert image file to bytes and add it to the list of image files
        with open(output_filename, "rb") as img_file:
            image_files.append(img_file)
        
    #output file
    with open("output_ocr.pdf","wb") as f:
        f.write(img2pdf.convert([img.name for img in image_files])) # Pass image file names (as bytes)
    print("Image converted to PDF successfully!")
    

easy_ocr("utpal.pdf","django")