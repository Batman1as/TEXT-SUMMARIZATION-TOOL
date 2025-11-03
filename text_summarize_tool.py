# text_summarization_tool.py
from transformers import pipeline

def summarize_text(text):
    # Load summarization pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("🔹 Welcome to the AI Text Summarization Tool 🔹")
    print("Type or paste your paragraph below (then press Enter):\n")

    text = input("📝 Enter your text here:\n")
    print("\n⏳ Generating summary...\n")
    result = summarize_text(text)
    print("✅ Summary generated successfully!\n")
    print(result)
