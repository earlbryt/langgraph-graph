import random
from typing import Literal
from typing import TypedDict
from IPython.display import Image, display, display_png
from langgraph.graph import StateGraph, START, END
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class State(TypedDict):
  graph_state: str
 
#Adds a string to the state message  
def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] +" I am"}
#Adds a string to the state message  
def node_2(state):
    print("---Node 2---")
    return {"graph_state": state['graph_state'] +" happy!"}
#Adds a string to the state message  
def node_3(state):
    print("---Node 3---")
    return {"graph_state": state['graph_state'] +" sad!"}
  
  
#Conditionally decides which node to visit next
def decide_mood(state) -> Literal["node_2", "node_3"]:
    
    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 
    
    # Here, let's just do a 50 / 50 split between nodes 2, 3
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "node_2"
    
    # 50% of the time, we return Node 3
    return "node_3"  
  

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Add
graph = builder.compile()

# View
# Get the graph visualization and display it
graph_image = graph.get_graph().draw_mermaid_png()
display_png(graph_image)

# Save the graph image to a file
with open("graph.png", "wb") as f:
    f.write(graph_image)


# Read and display the image using matplotlib
img = mpimg.imread('graph.png')
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()
