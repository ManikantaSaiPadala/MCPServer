#Recommended approach to create a client is to use the langchain client. This is a sample Python client that connects to the MCP server using langchain client.

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


async def main():

    #Create an instance of MultiServerMCPClient
    client = MultiServerMCPClient(

        #MCP Server config (JSON)
        {
            "mani_agentic_terminal": {
                            "transport": "stdio",
                            "command": "uvx",
                            "args": ["mani_agentic_terminal"]
                        }
                    
        }
        
    )

    tools = await client.get_tools()
    #print("Available tools:", tools)
    for tool in tools:
        print(f"Tool Name: {tool.name}")


if __name__ == "__main__":
    asyncio.run(main())