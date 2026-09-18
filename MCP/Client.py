from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from pathlib import Path
import os
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def main():
    # 1. Resolve absolute path for MathServer.py
    math_script_path = str(Path(__file__).parent / "MathServer.py")

    # 2. Initialize the client directly
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [math_script_path],
                "transport": "stdio",
            },
            "weather" : {
                "url":"http://127.0.0.1:8000/mcp", #ensure server is running here
                "transport":"streamable_http",          
            }
        }
    )
    
    # 3. Fetch the tools directly from the client object
    tools = await client.get_tools()

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    # 4. Use an active, supported Groq model name
    model = ChatGroq(model="openai/gpt-oss-20b")
    
    agent = create_react_agent(model, tools)

    # 5. Run the agent
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's (3+5) * 12?"}]}
    )

    print("Math Response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role":"user","content":"What is ther weather in california?"}]}
    )

    print("Weather response:", weather_response['messages'][-1].content)

asyncio.run(main())