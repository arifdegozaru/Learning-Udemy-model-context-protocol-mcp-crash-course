import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

stdio_server_parameters = StdioServerParameters(
    command='python',
    args=['C:/Users/arif_h667/learning/udemy/model-context-protocol/mcp-crash-course/servers/math_server.py']
)

async def main():
    print(os.getenv("OPEN_API_KEY"))
    print("Hello World")

if __name__ == '__main__':
    asyncio.run(main())