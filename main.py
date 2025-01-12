import random
from typing import Literal
from typing import TypedDict

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