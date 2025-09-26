# LangChain Summarization Project
A project to master LangChain through structured tasks.
Contributor: - Rooman

Task-1:
This task loads environment variables from a .env file using the dotenv library, retrieves Azure OpenAI configuration values (API key, endpoint, deployment name, and API version) from the environment, and prints them to the console.

Task-2:
This task imports two utility functions: one to configure an OpenAI language model and another to build a text summarizer. It sets up the language model, defines a passage about artificial intelligence, and creates two summarizers—one for a three-sentence summary and one for a single-sentence summary. It then prints both summaries of the AI passage using the respective summarizers.

Task-3:
This task loads a text file about AI, splits it into chunks, and stores their embeddings for retrieval. It then queries the vector store for text relevant to "AI milestones," summarizes the retrieved text into three sentences and one sentence using an LLM-based summarizer, and prints both summaries.

Task-4:
This task sets up an OpenAI language model and builds a three-sentence summarizer chain. It wraps the summarizer as a tool, adds it to an agent, and then uses the agent to summarize a passage about AI's impact on healthcare and to handle a vague summarization request. The results are printed to the console.

Task-5:
This task sets up an agent with tools for retrieving relevant text, summarizing it, and counting words. It loads a document, splits it into chunks, and creates embeddings. The agent is then used to find and summarize text about AI breakthroughs, and also to find, summarize, and count the words in the summary. The results are printed to the console.

Task-6:
This script demonstrates how to use LangChain's conversation memory modules to summarize and maintain context across multiple text inputs about machine learning and deep learning, printing summaries with both buffer and summary memory approaches.