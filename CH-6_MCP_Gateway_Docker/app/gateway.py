from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetchDataGateway():
    '''Use this tool to fetch data from a source...'''
    # Simulate fetching data from a database or an API
    data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is a sample data fetched from the server."
    }
    return data

@mcp.tool()
def processDataGateway(data):
    '''Use this tool to process the fetched data...'''
    # Simulate processing the data
    processed_data = {
        "id": data["id"],
        "name": data["name"].upper(),
        "description": data["description"].lower()
    }
    return processed_data


#Mount the tools to the MCP server/instance
mcp.mount(
    FastMCP.as_proxy({
        "mcpServers": {
            "ddg_mcp": {"command": "uvx", "args": ["duckduckgo-mcp-server"]}
            # "mani_agentic_terminal_mcp": {"command": "uvx", "args": ["mani_agentic_terminal"]},
        }
    })
)

mcp.mount(
    FastMCP.as_proxy({
        "mcpServers": {
            "mani_agentic_terminal_mcp": {"command": "uvx", "args": ["mani_agentic_terminal"]},
        }
    })
)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8092)  # Run the MCP server using streamable http...