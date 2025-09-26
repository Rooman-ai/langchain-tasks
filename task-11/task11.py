from utils.config_ai import configure_openai
from utils.init_agent import build_agent
from utils.tools import get_today_date, mock_web_search

llm = configure_openai()
tools = [get_today_date, mock_web_search]
agent = build_agent(tools, llm)

test_text = """Artificial Intelligence (AI) has rapidly evolved since the 1950s, achieving milestones
like expert systems, deep learning, and modern generative AI."""
print("=== Test 1 ===")
print(agent.run(f"Summarize this text: {test_text}. Also tell me today’s date."))
print("\n=== Test 2 ===")
print(agent.run("Summarize AI trends and search for recent updates."))
