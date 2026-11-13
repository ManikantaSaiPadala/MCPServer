#Recommended approach to create a client is to use the langchain client. This is a sample Python client that connects to the MCP server using langchain client.

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

async def main():

    #Create an instance of MultiServerMCPClient
    client = MultiServerMCPClient(

        #MCP Server config (JSON)
        {
            "duck_duck_go_mcp_stdio": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
    )

    tools = await client.get_tools()
    # print("Available tools:", tools)

    for tool in tools:
        print(f"Tool Name: {tool.name}")

    #Call the "search" tool with a query
    fetch_tool = tools[0]  # Assuming the first tool is the "search" tool
    query = "What is the capital of India?"
    result = await fetch_tool.ainvoke({"query": query})
    print(f"Tool Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())