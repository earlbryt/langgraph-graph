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