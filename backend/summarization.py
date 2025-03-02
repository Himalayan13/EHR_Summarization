from transformers import pipeline

# Load the summarization pipeline using BART (facebook/bart-large-cnn)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def chunk_text(text, max_words=800):
    """
    Splits text into chunks of approximately max_words.
    This helps if the input text is very long and exceeds model limits.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

def summarize_text(text):
    """
    Summarizes input text into a concise overall summary.
    If the text is long, it first splits it into chunks,
    summarizes each chunk, then combines those into a final summary.
    """
    # Split text into chunks if necessary
    chunks = chunk_text(text, max_words=800)
    intermediate_summaries = []
    
    for chunk in chunks:
        # Summarize each chunk
        summary = summarizer(chunk, max_length=60, min_length=30, do_sample=False)
        intermediate_summaries.append(summary[0]['summary_text'])
    
    # Combine the chunk summaries into one text
    combined_summary = " ".join(intermediate_summaries)
    
    # Summarize the combined summary into one overall sentence
    final_summary = summarizer(combined_summary, max_length=60, min_length=30, do_sample=False)[0]['summary_text']
    return final_summary

def read_text_file(file_path):
    """Reads text from the given file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    # Replace 'data/output/extracted_text.txt' with the path to your OCR output file.
    ocr_text = read_text_file("data/output/extracted2_text.txt")
    
    # Generate the overall patient history summary.
    patient_summary = summarize_text(ocr_text)
    
    print("Overall Patient History Summary:")
    print(patient_summary)




# from transformers import pipeline

# # Load the summarization model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def chunk_text(text, max_words=800):
#     """Splits text into chunks of approximately max_words."""
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), max_words):
#         chunk = " ".join(words[i:i+max_words])
#         chunks.append(chunk)
#     return chunks

# def summarize_prescriptions(text):
#     """
#     Generates a single generalized summary for all prescriptions combined.
#     """
#     # Split the text based on "### PRESCRIPTION BREAK ###"
#     prescriptions = text.split("### PRESCRIPTION BREAK ###")

#     # Remove empty entries and trim whitespace
#     prescriptions = [prescription.strip() for prescription in prescriptions if prescription.strip()]

#     # Combine all prescription texts into one document
#     combined_text = " ".join(prescriptions)

#     if not combined_text.strip():
#         return "No valid text found for summarization."

#     # Process in chunks if text is too long
#     chunks = chunk_text(combined_text, max_words=800)
#     intermediate_summaries = []

#     for chunk in chunks:
#         summary = summarizer(chunk, max_length=100, min_length=50, do_sample=False)
#         intermediate_summaries.append(summary[0]['summary_text'])

#     # Final overall summary
#     final_summary = " ".join(intermediate_summaries)
#     return final_summary


# !!!!!1

# from transformers import pipeline

# # Load the summarization pipeline using DistilBART
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# def chunk_text(text, max_words=800):
#     """Splits text into chunks of approximately max_words to fit model limits."""
#     words = text.split()
#     chunks = [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
#     return chunks

# def summarize_text(text):
#     """
#     Summarizes input text into a concise overall summary.
#     If text is long, it first splits it into chunks,
#     summarizes each chunk, then combines those into a final summary.
#     """
#     chunks = chunk_text(text, max_words=800)
#     intermediate_summaries = [summarizer(chunk, max_length=60, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]

#     # Combine chunk summaries and summarize again for final summary
#     combined_summary = " ".join(intermediate_summaries)
#     final_summary = summarizer(combined_summary, max_length=60, min_length=30, do_sample=False)[0]['summary_text']
#     return final_summary

