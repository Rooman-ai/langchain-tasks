from utils.config_ai import configure_openai
from utils.init_agent import build_agent
from utils.summarizer import build_summarizer
from utils.tools import make_text_summarizer_tool

llm=configure_openai()

three_sentence_chain = build_summarizer(llm,3)

text_summarizer_tool=make_text_summarizer_tool(three_sentence_chain,True)

tools = [text_summarizer_tool]

agent=build_agent(tools,llm)

healthcare_text = """
Artificial Intelligence (AI) is transforming healthcare by improving diagnostics, 
personalizing treatment plans, and predicting patient outcomes. Machine learning models 
analyze medical images faster and sometimes more accurately than doctors. AI-powered 
chatbots provide round-the-clock assistance, while predictive analytics help identify 
disease risks early. Robotics assist in surgeries with greater precision. However, 
concerns remain about patient privacy, bias in algorithms, and the need for regulatory 
frameworks. Despite these challenges, AI is enhancing healthcare efficiency, reducing 
costs, and ultimately saving lives by enabling doctors to make data-driven decisions 
more effectively and compassionately.
"""

print("\n=== Agent Run: Healthcare Impact ===")
print(agent.run(f"Summarize the impact of AI on healthcare: {healthcare_text}"))


print("\n=== Agent Run: Vague Request ===")
print(agent.run("Summarize something interesting"))
