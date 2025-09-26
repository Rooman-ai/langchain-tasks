from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_summarizer(llm, sentences=3):
    """Return a summarization chain that reduces text to given sentences."""
    template = f"Summarize the following text in exactly {sentences} sentences:\n\n{{text}}"
    prompt = PromptTemplate(input_variables=["text"], template=template)
    return LLMChain(llm=llm, prompt=prompt)

