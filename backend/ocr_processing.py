# import pytesseract
# import pdfplumber
# import cv2
# import os
# from PIL import Image

# # Set Tesseract path for Mac (if needed)
# # pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# def extract_text_from_image(image_path):
#     """Extract text from an image using Tesseract OCR."""
#     img = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#     text = pytesseract.image_to_string(img_gray)  # Perform OCR
#     return text

# def extract_text_from_pdf(pdf_path):
#     """Extract text from a PDF using pdfplumber (if text is selectable)."""
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             extracted_text = page.extract_text()
#             if extracted_text:
#                 text += extracted_text + "\n"
    
#     if text.strip():  
#         return text  # If text is found, return it

#     # If no selectable text, use OCR on images
#     print("🔍 No selectable text found. Using OCR...")
#     return extract_text_with_ocr(pdf_path)

# def extract_text_with_ocr(pdf_path):
#     """Extract text from image-based PDFs using Tesseract OCR."""
#     with pdfplumber.open(pdf_path) as pdf:
#         text = ""
#         for i, page in enumerate(pdf.pages):
#             image = page.to_image()
#             img_pil = image.original  # Get the image as a PIL object
#             img_cv = cv2.cvtColor(cv2.imread(img_pil.filename), cv2.COLOR_BGR2GRAY)

#             # Apply OCR
#             ocr_text = pytesseract.image_to_string(img_cv)
#             text += f"\n--- Page {i+1} ---\n" + ocr_text
    
#     return text

# def save_extracted_text(input_path, output_folder):
#     """Extracts text from a PDF or Image and saves it to a file."""
#     # Detect file type
#     if input_path.lower().endswith((".png", ".jpg", ".jpeg")):
#         print("🖼️ Processing an image file...")
#         text = extract_text_from_image(input_path)
#     elif input_path.lower().endswith(".pdf"):
#         print("📄 Processing a PDF file...")
#         text = extract_text_from_pdf(input_path)
#     else:
#         print("❌ Unsupported file format!")
#         return

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     output_path = os.path.join(output_folder, "extracted2_text.txt")
#     with open(output_path, "w") as f:
#         f.write(text)

#     print(f"✅ Text extraction complete! Check {output_path}")

# if __name__ == "__main__":
#     input_file = "/Users/himalayan_13/Desktop/CodeDump/EHR_Summarization/data/Prescription_1.pdf"  # Change to your image/pdf file
#     save_extracted_text(input_file, "/Users/himalayan_13/Desktop/CodeDump/EHR_Summarization/data/output")

# import pytesseract
# import pdfplumber
# import cv2
# import os
# import numpy as np
# from PIL import Image

# # Set Tesseract path if required (Mac/Linux users)
# # pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# def extract_text_from_image(image):
#     """Extract text from an image (PIL or OpenCV format) using Tesseract OCR."""
#     if isinstance(image, Image.Image):
#         image = np.array(image)  # Convert PIL image to NumPy array
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#     text = pytesseract.image_to_string(gray)  # Perform OCR
#     return text.strip()

# def extract_text_from_pdf(pdf_path):
#     """Extract text from a PDF. Uses pdfplumber for selectable text, OCR for scanned pages."""
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for i, page in enumerate(pdf.pages):
#             extracted_text = page.extract_text()
            
#             if extracted_text:
#                 text += f"\n--- Page {i+1} ---\n{extracted_text.strip()}\n\n"
#             else:
#                 print(f"🔍 No selectable text found on Page {i+1} of {pdf_path}. Using OCR...")
#                 text += extract_text_with_ocr(page, i)

#     return text.strip()

# def extract_text_with_ocr(page, page_number):
#     """Extracts text from an image-based PDF page using OCR."""
#     image = page.to_image().original  # Convert page to a PIL image
#     text = extract_text_from_image(image)
    
#     return f"\n--- OCR Extracted Page {page_number+1} ---\n{text}\n\n"

# def process_multiple_pdfs(pdf_paths, output_folder):
#     """Extracts text from multiple PDFs and saves it to a single file with separators."""
#     all_text = ""

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     for pdf_path in pdf_paths:
#         print(f"📄 Processing: {pdf_path}")
#         extracted_text = extract_text_from_pdf(pdf_path)

#         if extracted_text:
#             all_text += f"\n### PRESCRIPTION BREAK ###\n\n--- Extracted from {os.path.basename(pdf_path)} ---\n{extracted_text}\n\n"

#     # Save the combined text
#     output_path = os.path.join(output_folder, "combined_extracted_text.txt")
#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(all_text.strip())

#     print(f"✅ Text extraction complete! Check {output_path}")
#     return output_path  # Return the path to the extracted text file

# # Example usage
# if __name__ == "__main__":
#     pdf_files = ["uploaded_pdfs/sample1.pdf", "uploaded_pdfs/sample2.pdf"]  # List of PDFs
#     output_folder = "uploaded_pdfs"  # Folder to save extracted text
#     process_multiple_pdfs(pdf_files, output_folder)


import pytesseract
import pdfplumber
import cv2
import os
from PIL import Image

def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(img_gray)  # Perform OCR
    return text

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF using pdfplumber (if text is selectable)."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    
    if text.strip():  
        return text  # If text is found, return it

    # If no selectable text, use OCR on images
    return extract_text_with_ocr(pdf_path)

def extract_text_with_ocr(pdf_path):
    """Extract text from image-based PDFs using Tesseract OCR."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            image = page.to_image()
            img_pil = image.original  # Get the image as a PIL object
            img_cv = cv2.cvtColor(cv2.imread(img_pil.filename), cv2.COLOR_BGR2GRAY)

            # Apply OCR
            ocr_text = pytesseract.image_to_string(img_cv)
            text += f"\n--- Page {i+1} ---\n" + ocr_text
    
    return text

def save_extracted_text(input_path):
    """Extracts text from a PDF/Image and returns it (No file saving)."""
    if input_path.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(input_path)
    elif input_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(input_path)
    else:
        return "❌ Unsupported file format!"

    return text  # Directly return extracted text (API will handle response)
