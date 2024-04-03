import typer
from typing import Optional
import helpers

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello(name: str):
    "Connect with the project at .... url."
    print(f"Hello {name}")

#python src/cli/main.py build-standards openssf
@app.command()
def build_assesment(name: str):
    "Builds assessment using standards passed"
    print(f"Building Standards in /standards folder {name}")
    #TODO standards index
    # Open Standards
    file_and_path = 'tests/data/openssf_example.json'
    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = file.read()
    
    #TODO: Discovery functions
    print(standards_json)
    markdown = helpers.json_to_markdown_table(standards_json)
    helpers.open_write('/assessments/oveview_gap_analysis.md',markdown)

@app.command()
def build_standards(name: str):
    "Builds standards in the standards file."
    print(f"Building Standards in /standards folder {name}")

if __name__ == "__main__":
	app()