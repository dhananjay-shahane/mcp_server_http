# server.py
import os
from fastmcp import FastMCP
from mcp.types import TextContent
from scripts.bar_chart import generate_bar_chart

mcp = FastMCP(name="ChartServer")

SCRIPTS_FOLDER = "scripts"
OUTPUT_FOLDER = "output"

os.makedirs(SCRIPTS_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@mcp.tool(name="execute_chart_script", description="Executes the chart script and saves PNG output.")
async def execute_chart_script(output_file: str = "chart.png") -> TextContent:
    """
     Execute the this script\bar_chart.py.
    """
    try:
       generate_bar_chart() 
    except Exception as e:
        return TextContent(
            type="text",
            text=f"Error generating chart: {str(e)}"
        )

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000,
        path="/mcp"
    )
