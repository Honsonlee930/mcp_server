from fastmcp import FastMCP
app = FastMCP("My MCP Server")

@app.tool
def add(a:int,b:int)->int:
    """Add two numbers together"""
    return a + b
