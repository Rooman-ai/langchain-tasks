from datetime import datetime
from langchain.agents import tool

def make_text_summarizer_tool(three_sentence_chain,return_direct: bool = True):
    @tool("TextSummarizer", return_direct=return_direct)
    def text_summarizer_tool(text: str) -> str:
        """Summarizes the given text into concise sentences."""
        return three_sentence_chain.run(text)
    return text_summarizer_tool

def retreiver_tool(relevant_text_retriever,vectorstore,return_direct: bool = True):
    @tool("Retriever", return_direct=return_direct)
    def retriever_tool(query: str) -> str:
        """Retrieve relevant text chunks from the AI history document based on the query."""
        return relevant_text_retriever(vectorstore,query)
    return retriever_tool

def word_counter_tool(return_direct: bool = True):
    @tool("WordCounter", return_direct=return_direct)
    def word_counter_tool(text: str) -> str:
        """Counts the number of words in the given text."""
        count = len(text.split())
        return f"Word count: {count} and the summary is {text}"
    return word_counter_tool

@tool("get_today_date", return_direct=True)
def get_today_date(input_text: str) -> str:
    """Return today’s date (YYYY-MM-DD). Ignores the input_text."""
    return datetime.today().strftime("%Y-%m-%d")

@tool("mock web",return_direct=True)
def mock_web_search(query: str):
    """Mock AI web search returning static response."""
    return ("[Mock Search Result] Recent AI trends include advances in "
            "generative models, reinforcement learning, and ethical AI. ")
