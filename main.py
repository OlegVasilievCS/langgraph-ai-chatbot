import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

groq_key = os.getenv("groq_api_key")
lang_smith_key= os.getenv("lang_smith_api_key")

os.environ["LANGCHAIN_API_KEY"] = lang_smith_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"

llm = ChatGroq(groq_api_key=groq_key, model_name="llama-3.1-8b-instant")

class State(TypedDict):
    # Messages of are of type 'list'. The add_messages appends each message to
    #  the list, instead of overwritng. 
    messages: Annotated[list, add_messages]   

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": llm.invoke(state['messages'])}

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)