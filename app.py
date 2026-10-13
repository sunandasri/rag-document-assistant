
def answer_question(question, documents):
    """Find document text that may help answer a question."""
    if not question.strip():
        return "Please enter a question."

    if not documents:
        return "No documents are available."

    keywords = set(question.lower().split())
    matches = []

    for document in documents:
        text = document.strip()
        if not text:
            continue

        score = sum(
            word in text.lower()
            for word in keywords
            if len(word) > 2
        )

        if score > 0:
            matches.append((score, text))

    if not matches:
        return "I couldn't find relevant information in the provided documents."

    matches.sort(key=lambda item: item[0], reverse=True)
    return "\n\n".join(text for _, text in matches[:3])


if __name__ == "__main__":
    documents = [
        "RAG combines document retrieval with language models.",
        "Python is commonly used to build AI applications.",
        "FastAPI can expose Python functionality through REST APIs.",
    ]

    question = input("Ask a question: ")
    print("\nRetrieved context:")
    print(answer_question(question, documents))
