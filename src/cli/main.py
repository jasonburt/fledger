import typer
from typing import Optional
import helpers
import json

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello(name: str):
    "Connect with the project at .... url."
    print(f"Hello {name}")

#python src/cli/main.py build-skill-assessment openssf
@app.command()
def build_skill_assessment(name: str):
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
    skills_assment_matrix = helpers.mixin_skill_assessment_details(standards_json)
    markdown = helpers.json_to_markdown_table(skills_assment_matrix)
    helpers.open_write('/assessments/user/overview_skills_and_project_matrix.md',markdown)

@app.command()
def update_skill_assessment(name: str):
    "Updates skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")

#python src/cli/main.py build-project-assessment openssf
@app.command()
def build_project_assessment(name: str):
    "Builds repo standards assessment in the standards file."
    print(f"Building Standards in /assments/project folder {name}")
    # Open Standards
    file_and_path = 'tests/data/OpenSSF_Standards_Passing.json'
    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = json.load(file)
    project_assment_matrix = helpers.flatten_categories(standards_json)
    project_assessment_matrix = helpers.mixin_project_assessment_details(project_assment_matrix)
    #TODO: Discovery functions
    markdown = helpers.json_to_markdown_table(project_assessment_matrix)
    helpers.open_write('/assessments/project/overview_project_matrix.md',markdown)

#python src/cli/main.py search README --repo-path=Your/Cool/Repo --search-type=README
#python src/cli/main.py search 'README*' --search-type=file
@app.command()
def search(search: str, repo_path: str = '', search_type: str = 'code'):
	"Searches for a specific term in a repo."
	if search_type == 'code':
		results = helpers.search_term(search, repo_path)
	if search_type == 'file':
		print('FILE')
		results = helpers.search_files(search,repo_path)
	try:
		print(results)
	except:
		print('no search_type passed')

if __name__ == "__main__":
	app()