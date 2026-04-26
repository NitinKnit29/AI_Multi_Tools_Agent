from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .tools import web_search, calculator, get_weather
import os

def load_agent():
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = ChatOllama(model="llama3.2", temperature=0, base_url=ollama_base_url)
    
    tools = [web_search, calculator, get_weather]
    
    # Use proper message placeholders for tool-calling agent
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful AI assistant. You have access to tools that you can use to help answer questions.\n\n"
         "THINK CAREFULLY BEFORE USING A TOOL:\n"
         "- ONLY use get_weather if the user explicitly asks about weather or temperature (e.g., 'what is the weather in Delhi', 'how hot is it')\n"
         "- ONLY use calculator if the user explicitly asks for math or calculations (e.g., 'what is 2+2', 'calculate 15% of 100')\n"
         "- ONLY use web_search if the user asks about recent events or news (e.g., 'who won IPL 2019', 'latest news')\n\n"
         "DO NOT USE ANY TOOL FOR:\n"
         "- Greetings (hello, hi, hey)\n"
         "- Questions about your availability (are you available, can you help)\n"
         "- Questions about what you do (what can you do, who are you, what are your capabilities)\n"
         "- General conversation\n\n"
         "For these questions, answer directly and naturally WITHOUT using any tool."),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
    )
    return agent_executor
    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
    )
    return agent_executor
