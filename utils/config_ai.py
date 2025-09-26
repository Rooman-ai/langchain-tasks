import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
def configure_openai():
    load_dotenv()

    deployment = os.getenv("DEPLOYMENT_NAME")
    llm = AzureChatOpenAI(
    azure_deployment=deployment,
    temperature=0)
    return llm