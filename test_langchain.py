from app.core.langchain_llm import googleLLM

response = googleLLM.invoke(
    "Say hello"
)

print(
    response.content
)