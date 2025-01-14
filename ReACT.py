from langchain_groq import ChatGroq

# These 3 functions will be bound to the model as tools

# Tool 1: Multiply
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# Tool 2: Add
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

# Tool 3: Divide
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

# Define the tools as a list and initialize the model
tools = [add, multiply, divide]
llm = ChatGroq(model_name="llama-3.3-70b-versatile")

# Bind the tools to the model
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)