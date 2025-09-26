from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def history_summarizer(llm,memory):
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""
    You are a helpful summarizer.
    Conversation so far:
    {history}
    New text to summarize:
    {input}
    Give a concise summary (3-4 sentences).
    """
    )
    buffer_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
    return buffer_chain