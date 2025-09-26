from utils.config_ai import configure_openai
from utils.text_loader import load_text
from utils.summarizer import build_summarizer
from utils.qa import build_qa_chain

llm = configure_openai()
text = load_text()

summarizer = build_summarizer(llm,3)
summary = summarizer.run(text)

qa_chain = build_qa_chain(llm)

print("=== On Summary ===")
print(qa_chain.run({"text": summary, "question": "What’s the key event mentioned?"}))

print("\n=== On Full Text ===")
print(qa_chain.run({"text": text, "question": "What’s the key event mentioned?"}))
