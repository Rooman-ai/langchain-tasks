from langchain.document_loaders import PyPDFLoader,WebBaseLoader
from utils.config_ai import configure_openai
from utils.config_embedding import configure_embedding
from utils.text_splitter_store import text_splitter_store
from utils.retriever import relevant_text_retriever
from utils.summarizer import build_summarizer

llm=configure_openai()

embeddings=configure_embedding()
web_url = "https://www.cloudflight.io/en/blog/ai-trends-2024/"

pdf_path=pdf_path = "C:\\Users\\Administrator\\Downloads\\Policy-Brief-AI-Ethics_0.pdf"

pdf_load=PyPDFLoader(pdf_path)
pdf_docs=pdf_load.load()

web_content=WebBaseLoader(web_url)
web_docs=web_content.load()

pdf_vector=text_splitter_store(embeddings,pdf_docs,chunk_size=150, overlap=30)
web_vector=text_splitter_store(embeddings,web_docs,chunk_size=150, overlap=30)
query="AI challenges"
pdf_retreiver=relevant_text_retriever(pdf_vector,query)
web_retreiver=relevant_text_retriever(web_vector,query)

summarizer_chain=build_summarizer(llm,3)

res1=summarizer_chain.run({"text":pdf_retreiver})
print("pdf:",res1)

res2=summarizer_chain.run({"text":web_retreiver})
print("web:",res2)


