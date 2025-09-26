from utils.summarizer import build_summarizer
from utils.config_embedding import configure_embedding
from utils.config_ai import configure_openai
from utils.text_loader import load_text
from utils.text_splitter_store import text_splitter_store
from utils.retriever import relevant_text_retriever

llm=configure_openai()
embeddings=configure_embedding()
documents=load_text("text_files/ai_intro.txt")

vectorstore=text_splitter_store(embeddings,documents,200, 20)

query = "AI milestones"

retrieved_text=relevant_text_retriever(vectorstore,query)

three_sentence_summarizer=build_summarizer(llm,3)
one_sentence_summarizer=build_summarizer(llm,1)


print("\n=== 3 Sentence Summary ===")
print(three_sentence_summarizer.run(retrieved_text))

print("\n=== 1 Sentence Summary ===")
print(one_sentence_summarizer.run(retrieved_text))
