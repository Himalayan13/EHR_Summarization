from flask import Flask, request, jsonify
from ocr_processing import extract_text_from_pdf  # Your OCR module function
from summarization import summarize_text           # Your summarization module function

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_prescription():
    # Get file from request
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # Save the file temporarily
    file_path = "temp_prescription.pdf"
    file.save(file_path)

    # Run OCR to extract text
    ocr_text = extract_text_from_pdf(file_path)
    
    # Run summarization
    summary = summarize_text(ocr_text)
    
    # Return the summary
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask, request, jsonify
# import os
# from ocr_processing import process_multiple_pdfs  # OCR function for multiple PDFs
# from summarization import summarize_prescriptions  # Updated summarization function

# app = Flask(__name__)

# UPLOAD_FOLDER = "uploaded_pdfs"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload folder exists

# @app.route('/summarize', methods=['POST'])
# def summarize_prescriptions_api():
#     files = request.files.getlist('files')  # Get multiple files from request
#     if not files or len(files) == 0:
#         return jsonify({"error": "No files provided"}), 400

#     # Save uploaded PDFs temporarily
#     pdf_paths = []
#     for file in files:
#         file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(file_path)
#         pdf_paths.append(file_path)

#     # Extract text from all PDFs
#     extracted_text_path = process_multiple_pdfs(pdf_paths, UPLOAD_FOLDER)

#     # Read extracted text from file
#     with open(extracted_text_path, "r", encoding="utf-8") as f:
#         ocr_text = f.read().strip()

#     if not ocr_text:
#         return jsonify({"error": "No text extracted from PDFs"}), 400

#     # Run enhanced summarization for separate prescriptions
#     summary = summarize_prescriptions(ocr_text)

#     # Return the summary
#     return jsonify({"summary": summary})

# if __name__ == "__main__":
#     app.run(debug=True)

