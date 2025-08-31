import os
from fastmcp import FastMCP
from mcp.types import TextContent
from scripts.bar_chart import generate_bar_chart

mcp = FastMCP(name="ChartServer")

SCRIPTS_FOLDER = "scripts"
OUTPUT_FOLDER = "output"

# Ensure folders exist
os.makedirs(SCRIPTS_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@mcp.tool(name="execute_chart_script", description="Generates a bar chart and saves it as a PNG file.")
async def execute_chart_script(output_file: str = "chart.png") -> TextContent:
    """
    Executes the bar_chart.py script and saves chart as PNG.
    """
    try:
        output_path = os.path.join(OUTPUT_FOLDER, output_file)
        generate_bar_chart(output_path)   # bar_chart.py saves chart here
        return TextContent(
            type="text",
            text=f"✅ Chart generated successfully: {output_path}"
        )
    except Exception as e:
        return TextContent(
            type="text",
            text=f"❌ Error generating chart: {str(e)}"
        )

if __name__ == "__main__":
    # Let fastmcp.cloud handle transport, don't hardcode host/port
    mcp.run()
