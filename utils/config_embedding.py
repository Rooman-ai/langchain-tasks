import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
def configure_embedding():
    load_dotenv()
    deployment = os.getenv("deployment")
    embedding= AzureOpenAIEmbeddings(
    azure_deployment=deployment)
    return embedding