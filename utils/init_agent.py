from langchain.agents import initialize_agent, AgentType

def build_agent(tools, llm, verbose=True):
    """Return a LangChain agent with given tools."""
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=verbose
    )
