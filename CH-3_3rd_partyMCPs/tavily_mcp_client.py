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
            "tavily_mcp_http": {
                "transport": "http",
                "url": "https://mcp.tavily.com/mcp/",
                "headers": {
                    "Authorization": f"Bearer {os.environ['TAVILY_API_KEY']}"
                }
            }
                    
        }
        
    )

    tools = await client.get_tools()
    print("Available tools:", tools)


if __name__ == "__main__":
    asyncio.run(main())