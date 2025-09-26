from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from utils.config_ai import configure_openai
from utils.build_history_summarizer import history_summarizer

llm = configure_openai()

print("\n=== Using ConversationBufferMemory ===\n")
buffer_memory = ConversationBufferMemory(k=3,memory_key="history")

buffer_chain=history_summarizer(llm,buffer_memory)

ml_text = """Machine learning is a field of artificial intelligence that focuses on building systems
that can learn from data and improve their performance over time without being explicitly programmed.
It involves algorithms that identify patterns in large datasets and use them for tasks like prediction,
classification, and decision-making. Machine learning has applications in recommendation systems,
speech recognition, image classification, fraud detection, and natural language processing."""

dl_text = """Deep learning is a subset of machine learning that uses artificial neural networks with many layers
to model complex patterns in data. These networks automatically extract features from raw input,
reducing the need for manual feature engineering. Deep learning has enabled breakthroughs in computer vision,
natural language understanding, autonomous driving, and generative AI models such as GPT and DALL·E."""

print("First Summary (ML):")
print(buffer_chain.run(ml_text))

print("\nSecond Summary (DL, with ML context):")
print(buffer_chain.run(dl_text))

print("\n=== Using ConversationSummaryMemory ===\n")
summary_memory = ConversationSummaryMemory(
    llm=llm, memory_key="history"
)

summary_chain=history_summarizer(llm,summary_memory)

print("First Summary (ML):")
print(summary_chain.run(ml_text))

print("\nSecond Summary (DL, with ML context):")
print(summary_chain.run(dl_text))
