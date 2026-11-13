#This is a sample Python client that connects to the MCP server using stdio (Raw method type to create a client).

import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio

# Path to the MCP server script
server_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1_first_mcp_server_stdio.py')
print(f"Server script path: {server_script_path}")

# Create a server parameters
server_params = StdioServerParameters(
    command = "python",
    args = [str(server_script_path)],
    env = {}
    )


# Create a client session
async def main():
    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            #Fetch the tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            #Call ProcessData tool
            data = await session.call_tool("processData", {"data": {"id": 1, "name": "Sample Data", "description": "This is a sample data fetched from the server."}})
            print("Processed Data:", data)

if __name__ == "__main__":
    asyncio.run(main())