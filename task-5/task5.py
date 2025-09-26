from utils.init_agent import initialize_agent
from utils.config_ai import configure_openai
from utils.config_embedding import configure_embedding
from utils.text_loader import load_text
from utils.text_splitter_store import text_splitter_store
from utils.summarizer import build_summarizer
from utils.retriever import relevant_text_retriever
from utils.tools import make_text_summarizer_tool
from utils.tools import retreiver_tool
from utils.tools import word_counter_tool

llm=configure_openai()

embeddings = configure_embedding()

documents=load_text("text_files/ai_intro.txt")

vectorstore = text_splitter_store(embeddings,documents,chunk_size=200, overlap=20)

three_sentence_chain = build_summarizer(llm,3)

text_summarizer_tool=make_text_summarizer_tool(three_sentence_chain,False)
retriever_tool=retreiver_tool(relevant_text_retriever,vectorstore,False)
word_counter_tool=word_counter_tool(True)

tools = [retriever_tool, text_summarizer_tool, word_counter_tool]

agent =initialize_agent(tools,llm)

print("\n=== Agent Run: Find and Summarize ===")
result = agent.run("Find and summarize text about AI breakthroughs from the document.")
print(result)

print("\n=== Agent Run: Find, Summarize, and Count ===")
result = agent.run("Find and summarize text about AI breakthroughs from the document. Then count the words in the summary.")
print(result)
