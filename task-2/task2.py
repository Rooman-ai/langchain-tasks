from utils.summarizer import build_summarizer
from utils.config_ai import configure_openai

llm=configure_openai()

text_about_ai = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are designed to think, learn, and adapt like humans. 
These systems can perform tasks such as recognizing speech, making decisions, and identifying patterns in data. 
AI is typically categorized into two main types: narrow AI, which is specialized for a particular task such as language translation or facial recognition, 
and general AI, which would be capable of performing a wide range of tasks at the level of human intelligence. 
Recent advancements in machine learning, especially deep learning, have accelerated the growth of AI, 
enabling breakthroughs in fields such as healthcare, autonomous vehicles, finance, and robotics. 
For example, AI can assist doctors in diagnosing diseases more accurately, power self-driving cars, 
and detect fraudulent transactions in real time. Despite these benefits, AI also poses significant challenges, 
including ethical concerns, job displacement, and the potential misuse of intelligent systems. 
Researchers and policymakers are actively working to ensure that AI development is safe, fair, and beneficial to society. 
The future of AI holds immense potential, but it requires careful regulation and responsible innovation to maximize benefits while minimizing risks.
"""

three_sentence_summarizer=build_summarizer(llm,3)
one_sentence_summarizer=build_summarizer(llm,1)


print("\n=== 3 Sentence Summary ===")
print(three_sentence_summarizer.run(text_about_ai))

print("\n=== 1 Sentence Summary ===")
print(one_sentence_summarizer.run(text_about_ai))