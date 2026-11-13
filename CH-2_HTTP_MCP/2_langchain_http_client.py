#Recommended approach to create a client is to use the langchain client. This is a sample Python client that connects to the MCP server using langchain client.

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

# Path to the MCP server script
server_script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'CH-1_CreateMCP', '1_first_mcp_server_stdio.py')
print(f"Server script path: {server_script_path}")

#Path to the virtual environment python executable
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.venv', 'Scripts', 'python.exe')
print(f"Virtual environment python executable path: {venv_path}")

async def main():

    #Create an instance of MultiServerMCPClient
    client = MultiServerMCPClient(

        #MCP Server config (JSON)
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": venv_path,
                "args": [str(server_script_path)],
                "env": {}
            },
            "data_fetch_mcp_http": {
                "transport": "streamable-http",
                "url": "http://localhost:8090/mcp"
            }
                    
        }
        
    )

    tools = await client.get_tools()
    print("Available tools:", tools)


if __name__ == "__main__":
    asyncio.run(main())