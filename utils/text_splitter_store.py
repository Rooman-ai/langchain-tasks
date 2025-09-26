from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS

def text_splitter_store(embeddings,documents,chunk_size=200, overlap=20,separator=""):
    """Return a text splitter for document chunking."""
    text_splitter=CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separator=separator
    )
    docs = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
