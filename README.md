# 📄 AI-Powered Electronic Health Record (EHR) Summarization
![image](https://github.com/user-attachments/assets/8c727e4e-09fb-484e-8865-9003b7050600)


## 🚀 Project Overview

This project is an **AI-powered EHR summarization system** designed to help **doctors quickly review** patient history by summarizing past prescriptions and medical records. The system extracts text from scanned prescription PDFs using **OCR**, processes the data, and generates a concise summary using a **BART-based summarization model**.

The **frontend is built using Streamlit**, while the backend is powered by **Flask**, integrating OCR, text processing, and AI-based summarization.

---

## 📌 Features
- **Optical Character Recognition (OCR):** Extracts text from scanned medical prescriptions.
- **AI-based Summarization:** Utilizes **BART (Bidirectional and Auto-Regressive Transformers)** to summarize extracted text.
- **Flask API Integration:** Serves as a backend pipeline for processing the OCR-extracted text and generating summaries.
- **Streamlit Frontend:** Provides a simple and user-friendly interface for uploading prescription PDFs and displaying the summarized output.
- **Seamless Workflow:** From file upload to summarized report generation in just a few clicks.

---

## 🛠️ Tech Stack

### **Backend**
- **Python** - Core programming language
- **Flask** - API development
- **OCR (PyMuPDF, pdf2image, or Tesseract)** - Extracts text from PDFs
- **Transformers (Hugging Face)** - AI-based text summarization using **BART**
- **NLTK / SpaCy** - Text preprocessing

### **Frontend**
- **Streamlit** - Interactive UI for uploading files and displaying summaries

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
 git clone https://github.com/Himalayan13/EHR_Summarization.git
 cd EHR_Summarization
```

### **2️⃣ Install Dependencies**
```bash
 pip install -r requirements.txt
```

### **3️⃣ Start the Backend (Flask API)**
```bash
 python backend/api.py
```

### **4️⃣ Start the Frontend (Streamlit App)**
```bash
 streamlit run main.py
```

---

## 🔄 Workflow
1. **Upload a medical prescription PDF** via the Streamlit interface.
2. The **Flask API** processes the PDF using OCR and extracts text.
3. The extracted text is passed to a **BART-based summarization model**.
4. A concise medical summary is generated and displayed in the frontend.

---

## 📊 Performance Metrics
To evaluate the quality of summarization, we used:
- **ROUGE Score** - Measures text overlap between original and summary.
- **BLEU Score** - Evaluates the accuracy of AI-generated summaries compared to human-written ones.

---

## 🔮 Future Improvements
🔹 **Integrating IoT** for **automatic scanning of prescriptions** in hospitals.
🔹 **Developing a custom medical NER (Named Entity Recognition) model** for more accurate entity extraction.
🔹 **Expanding support for multilingual prescriptions**.

---

## 🎯 Contributors
- **Himnish A** - AI & Backend Development
- **Shaurya Rathore** - Frontend Development
- **Aadya Chopra, Mayank Singh** - API Integration

---

## 📬 Contact
For any queries, feel free to reach out at **himnisha11@gmail.com** or create an issue in the GitHub repository.

---

## 🏆 Acknowledgments
Special thanks to **Hugging Face** for providing state-of-the-art NLP models and **Streamlit** for simplifying the frontend development process.

---

🚀 **Transforming Healthcare with AI!**

