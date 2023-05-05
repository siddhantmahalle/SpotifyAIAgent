import os
from typing import List

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from consts import llm_model_type

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(max_retries=3, temperature=0, model_name=llm_model_type)

def initialize_agent_zero_shot(tools: List, is_agent_verbose: bool = True, max_iterations: int = 3, return_thought_process: bool = True):
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, 
                             verbose=is_agent_verbose, max_iterations=max_iterations, 
                             return_thought_process=return_thought_process, memory=memory)

    return agent

