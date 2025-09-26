from langchain_community.document_loaders import TextLoader

def load_text(file_path="text_files/ai_intro.txt"):
    """Load text file and return full content as string."""
    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()
    return docs
