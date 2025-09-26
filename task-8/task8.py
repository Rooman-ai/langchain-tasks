from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from utils.config_ai import configure_openai

llm = configure_openai()

responseSchema=[ResponseSchema(name="summary",description="summary of text"),
                ResponseSchema(name="length",description="The character count of the summary")]
outputparser=StructuredOutputParser.from_response_schemas(responseSchema)
formatInstructions=outputparser.get_format_instructions()
prompt = PromptTemplate(
    template=(
        "Summarize the following text in 3 sentences:\n\n"
        "{text}\n\n"
        "Format the response as JSON with the following keys:\n"
        "{format_instructions}"
    ),
    input_variables=["text"],
    partial_variables={"format_instructions": formatInstructions},
)

chain=prompt | llm | outputparser
ai_text = """
Artificial Intelligence (AI) is rapidly transforming industries worldwide by automating tasks,
enhancing decision-making, and driving innovation. In healthcare, AI assists in disease diagnosis,
drug discovery, and personalized treatment recommendations. Financial services rely on AI for fraud
detection, algorithmic trading, and customer support through chatbots. Manufacturing companies adopt
AI for predictive maintenance, quality control, and process optimization. Education has embraced AI
through adaptive learning platforms and virtual tutors that personalize student experiences.
Transportation is seeing AI-powered self-driving vehicles and traffic management systems that
improve safety and efficiency. Retail benefits from AI in customer behavior analysis, product
recommendations, and inventory optimization. Government agencies employ AI for public safety,
resource allocation, and policy analysis. Despite its advantages, AI raises ethical concerns such as
job displacement, privacy risks, and algorithmic bias. Addressing these challenges while leveraging
AI's potential is essential for building a sustainable, equitable future.
"""
result=chain.invoke({"text":ai_text})
print(result)