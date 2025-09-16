import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command='python',
    args=['C:/Users/arif_h667/learning/udemy/model-context-protocol/mcp-crash-course/servers/math_server.py']
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session) # load mcp tools and adapted tools to llm tools

            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke({'messages': HumanMessage(content='What is 54 + 2 * 3?')})
            print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())