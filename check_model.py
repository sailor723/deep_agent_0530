from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import sys

try:
    print("Initializing model...")
    model = init_chat_model(
        "qwen3:14b",
        model_provider="openai",
        base_url="http://localhost:11434/v1",
        openai_api_key="ollama",
        temperature=0.0,
    )
    
    print("Invoking model...")
    response = model.invoke([HumanMessage(content="Hi")])
    print(f"Response: {response.content}")
    print("Model working successfully.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
