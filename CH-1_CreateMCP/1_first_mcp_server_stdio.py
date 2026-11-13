from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetchData():
    '''Use this tool to fetch data from a source...'''
    # Simulate fetching data from a database or an API
    data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is a sample data fetched from the server."
    }
    return data

@mcp.tool()
def processData(data):
    '''Use this tool to process the fetched data...'''
    # Simulate processing the data
    processed_data = {
        "id": data["id"],
        "name": data["name"].upper(),
        "description": data["description"].lower()
    }
    return processed_data

if __name__ == "__main__":
    mcp.run(transport="stdio")  # Run the MCP server using standard input/output