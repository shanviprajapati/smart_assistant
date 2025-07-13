from transformers import pipeline
import pdfplumber

# Initialize the summarizer model
summarizer = pipeline("summarization")

def extract_text(content):
    """uploaded PDF content."""
    with open("temp.pdf", "wb") as f:
        f.write(content)

    with pdfplumber.open("temp.pdf") as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    if not text.strip():
        raise ValueError("PDF has no readable text.")

    return text

def generate_summary(content):
    """summary."""
    text = extract_text(content)

    if not text or text.strip() == "":
        return "found in the PDF."

   
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = []

    for chunk in chunks[:3]:  
        try:
            result = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
            if result and isinstance(result, list):
                summaries.append(result[0]['summary_text'])
        except Exception as e:
            print(" failed:", e)
            summaries.append("not summarize.")

    if summaries:
        return "\n\n".join(summaries)
    else:
        return "Error"