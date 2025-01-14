from langchain_groq import ChatGroq
from langgraph.graph import MessagesState  # Predefined state schema with a single parameter: a list of messages. 
# As well as logic to append messages to the state at each node or edge
from langchain_core.messages import HumanMessage, SystemMessage  # Prompt templates

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


# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

# Node
def assistant(state: MessagesState): # The state is a list of messages
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]} # Add the new messages to the system message and invoke the model_with_tools
