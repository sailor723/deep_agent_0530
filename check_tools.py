from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import sys

@tool
def magic_function(input: str) -> str:
    """Do magic."""
    return "Magic!"

try:
    print("Initializing model...")
    model = init_chat_model(
        "qwen3:14b",
        model_provider="openai",
        base_url="http://localhost:11434/v1",
        openai_api_key="ollama",
        temperature=0.0,
    )
    
    print("Binding tools...")
    model_with_tools = model.bind_tools([magic_function])
    
    print("Invoking model with tool request...")
    response = model_with_tools.invoke([HumanMessage(content="Call the magic function with input 'hocus pocus'")])
    
    print(f"Response type: {type(response)}")
    print(f"Response content: {response.content}")
    print(f"Tool calls: {response.tool_calls}")
    
    if response.tool_calls:
        print("SUCCESS: Tool call generated.")
    else:
        print("WARNING: No tool call generated.")

except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
