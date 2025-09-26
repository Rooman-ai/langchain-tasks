from langchain.retrievers.multi_query import MultiQueryRetriever
from utils.config_ai import configure_openai
from utils.config_embedding import configure_embedding
from utils.text_loader import load_text
from utils.text_splitter_store import text_splitter_store
from utils.summarizer import build_summarizer
from utils.retriever import relevant_text_retriever

llm=configure_openai()
embedding=configure_embedding()

docs=load_text("text_files/ai_intro.txt")
vectors=text_splitter_store(embedding,docs,200,20)

retreiver2=MultiQueryRetriever.from_llm(retriever=vectors.as_retriever(search_kwargs={"k": 3}),
    llm=llm,
    )

chain=build_summarizer(llm,3)
query = "AI advancements"

single_docs=relevant_text_retriever(vectors,query)
res1=chain.run({"text":single_docs})
print("Single  Query Response:",res1)

multi_query=retreiver2.get_relevant_documents(query)
multi_docs=" ".join(doc.page_content for doc in multi_query )
res2=chain.run({"text":multi_docs})
print("Multiple  Query Response:",res2)