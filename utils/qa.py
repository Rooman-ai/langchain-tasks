from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_qa_chain(llm):
    """Return QA chain that answers questions based on text."""
    template = """Answer the question based on the text:

    Text:
    {text}

    Question:
    {question}

    Answer:"""
    prompt = PromptTemplate(input_variables=["text", "question"], template=template)
    return LLMChain(llm=llm, prompt=prompt)
