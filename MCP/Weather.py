from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather of the location specified."""
    return "It's always raining in Switz."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

"""INFO:     Started server process [12147]
INFO:     Waiting for application startup.
StreamableHTTP session manager started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
"""