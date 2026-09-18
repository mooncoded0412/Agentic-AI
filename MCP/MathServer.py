from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)-> int:
    """_summary_
     Add 2 numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int)-> int:
    """Multiply 2 numbers"""
    return a*b

#The transport = "stdio" argument tells the server to:

#Use standard input/output (stdin and stdout) to receive and respond to tool function calls (through command line/ terminal for local testing purposes and all..)

if __name__=="__main__":
    mcp.run(transport="stdio")