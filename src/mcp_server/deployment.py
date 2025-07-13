from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def add_two_numbers(a:int, b:int)->int:
    """Add two numbers together"""
    return a + b