import pytesseract
import pdfplumber
import cv2
import os
from PIL import Image

# Set Tesseract path for Mac (if needed)
# pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

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
    print("🔍 No selectable text found. Using OCR...")
    return extract_text_with_ocr(pdf_path)

def extract_text_with_ocr(pdf_path):
    """Extract text from image-based PDFs using Tesseract OCR."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for i, page in enumerate(pdf.pages):
            image = page.to_image()
            img_pil = image.original  # Get the image as a PIL object
            img_cv = cv2.cvtColor(cv2.imread(img_pil.filename), cv2.COLOR_BGR2GRAY)

            # Apply OCR
            ocr_text = pytesseract.image_to_string(img_cv)
            text += f"\n--- Page {i+1} ---\n" + ocr_text
    
    return text

def save_extracted_text(input_path, output_folder):
    """Extracts text from a PDF or Image and saves it to a file."""
    # Detect file type
    if input_path.lower().endswith((".png", ".jpg", ".jpeg")):
        print("🖼️ Processing an image file...")
        text = extract_text_from_image(input_path)
    elif input_path.lower().endswith(".pdf"):
        print("📄 Processing a PDF file...")
        text = extract_text_from_pdf(input_path)
    else:
        print("❌ Unsupported file format!")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "extracted_text.txt")
    with open(output_path, "w") as f:
        f.write(text)

    print(f"✅ Text extraction complete! Check {output_path}")

if __name__ == "__main__":
    input_file = "//Users/himalayan_13/Desktop/CodeDump/EHR_Summarization/data/parchi.jpg"  # Change to your image/pdf file
    save_extracted_text(input_file, "/Users/himalayan_13/Desktop/CodeDump/EHR_Summarization/data/output")
