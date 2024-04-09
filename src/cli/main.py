import typer
from typing import Optional
try:
	from  cli import helpers
except:
	import helpers


import json

app = typer.Typer(no_args_is_help=True)

@app.command()
def getting_started(name: str):
    "Getting Started"
    print(f"Hello! Welcome to fledger! To get started read the README for a list of example and connect with the project at https://github.com/jasonburt/fledger.")

#python cli/main.py build-skill-assessment OpenSSF_Standards_Passing
@app.command()
def build_skill_assessment(name: str):
    "Builds skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")
    #TODO standards index
    # Open Standards
    file_and_path = 'tests/data/'+name+'.json'

    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = json.load(file)
    #TODO: Discovery functions
    # print(standards_json)
    skills_assment_matrix = helpers.flatten_categories(standards_json)
    skills_assment_matrix = helpers.mixin_skill_assessment_details(skills_assment_matrix)
    markdown = helpers.json_to_markdown_table(skills_assment_matrix)
    helpers.open_write('/assessments/user/overview_skills_and_project_matrix.md',markdown)
    print('Build Complete')

@app.command()
def update_skill_assessment(name: str):
    "Updates skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")

#python cli/main.py build-project-assessment TwilioAITRust
#python cli/main.py build-project-assessment OpenSSF_Standards_Passing
@app.command()
def build_project_assessment(name: str):
    "Builds repo standards assessment in the standards file."
    print(f"Building Standards in /assments/project folder {name}")
    # Open Standards
    file_and_path = 'tests/data/'+name+'.json'
    #Convert to markdown
    with open(file_and_path, 'r', encoding='utf-8') as file:
    	standards_json = json.load(file)
    project_assment_matrix = helpers.flatten_categories(standards_json)
    project_assessment_matrix = helpers.mixin_project_assessment_details(project_assment_matrix)
    #TODO: Discovery functions
    markdown = helpers.json_to_markdown_table(project_assessment_matrix)
    helpers.open_write('/assessments/project/overview_project_matrix.md',markdown)

#python cli/main.py search README --repo-path=Your/Cool/Repo --search-type=file
#python cli/main.py search 'README*' --search-type=file
#python cli/main.py search 'README*' --search-type=file -save
@app.command()
def search(search: str, repo_path: str = '', search_type: str = 'code', save: bool = False):
	"Searches for a specific term in a repo."
	if search_type == 'code':
		results = helpers.search_term(search, repo_path)
	if search_type == 'file':
		results = helpers.search_files(search,repo_path)
	if results:
		#TODO: For long files show short list.
		print(str(len(results)) + ' records found. First record below.')
		print(json.dumps(results[0],indent=4))
	else:
		print('No results found, change search paramaters.')
	if save:
			#TODO fix this
			name = search
			save_path = helpers.record_struct(name,search,results)
			print('Record Recorded at '+save_path)

if __name__ == "__main__":
	app()