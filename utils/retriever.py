def relevant_text_retriever(vectorstore,query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    retrieved_docs = retriever.get_relevant_documents(query)
    retrieved_text = " ".join([doc.page_content for doc in retrieved_docs])
    return retrieved_text
    