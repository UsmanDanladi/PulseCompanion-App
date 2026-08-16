import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def build_knowledge_base(docs_folder):
    knowledge_base = []
    for filename in os.listdir(docs_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(docs_folder, filename)
            print(f"Reading: {filename}")
            text = extract_text_from_pdf(pdf_path)
            knowledge_base.append({
                "source": filename,
                "content": text
            })
    return knowledge_base

def search_knowledge_base(query, knowledge_base):
    results = []
    query_words = query.lower().split()
    for doc in knowledge_base:
        content_lower = doc["content"].lower()
        score = sum(1 for word in query_words if word in content_lower)
        if score > 0:
            results.append({
                "source": doc["source"],
                "score": score,
                "excerpt": doc["content"][:500]
            })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:3]

if __name__ == "__main__":
    docs_folder = "."
    kb = build_knowledge_base(docs_folder)
    print(f"Loaded {len(kb)} documents")
    results = search_knowledge_base("AI health", kb)
    for r in results:
        print(f"Source: {r['source']}, Score: {r['score']}")
        print(f"Excerpt: {r['excerpt'][:200]}")
        print("---")