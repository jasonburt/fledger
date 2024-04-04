import typer
from typing import Optional
import helpers
import json

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello(name: str):
    "Connect with the project at .... url."
    print(f"Hello {name}")

#python src/cli/main.py build-standards openssf
@app.command()
def build_skill_assesment(name: str):
    "Builds skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")
    #TODO standards index
    # Open Standards
    file_and_path = 'tests/data/openssf_example.json'
    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = json.load(file)
    #TODO: Discovery functions
    print(standards_json)
    skills_assment_matrix = helpers.mixin_skill_assesment_details(standards_json)
    markdown = helpers.json_to_markdown_table(skills_assment_matrix)
    helpers.open_write('/assessments/user/overview_skills_and_project_matrix.md',markdown)

@app.command()
def update_skill_assesment(name: str):
    "Updates skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")

#python src/cli/main.py build-project-assesment openssf
@app.command()
def build_project_assesment(name: str):
    "Builds repo standards assessment in the standards file."
    print(f"Building Standards in /assments/project folder {name}")
    # Open Standards
    file_and_path = 'tests/data/OpenSSF_Standards_Passing.json'
    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = json.load(file)
    project_assment_matrix = helpers.flatten_categories(standards_json)
    project_assesment_matrix = helpers.mixin_project_assesment_details(project_assment_matrix)
    #TODO: Discovery functions
    markdown = helpers.json_to_markdown_table(project_assesment_matrix)
    helpers.open_write('/assessments/project/overview_skills_and_project_matrix.md',markdown)

if __name__ == "__main__":
	app()