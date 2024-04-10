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

#python src/cli/main.py build-skill-assessment OpenSSF_Standards_Passing
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
    print(standards_json)
    skills_assment_matrix = helpers.flatten_categories(standards_json)
    skills_assment_matrix = helpers.mixin_skill_assessment_details(skills_assment_matrix)
    markdown = helpers.json_to_markdown_table(skills_assment_matrix)
    helpers.open_write('/assessments/user/overview_skills_and_project_matrix.md',markdown)

#python src/cli/main.py update-skill-assessment Documentation Detailed search 'README*' --search-type=file
#python cli/main.py update-skill-assessment Documentation Detailed search 'README*' --search-type=file
#python cli/main.py update-skill-assessment Basics Documentation search 'README*' --search-type=file
@app.command()
def update_skill_assessment(category: str, subcat: str, command: str, search: str, repo_path: str = '', search_type: str = 'code'):
    "Updates skill assessment using standards passed."
    col_index = 0
    letter_index = 0
    print(f"Updating section {category}:{subcat} with {command}:{search}...")
    file_and_path = '../assessments/user/overview_skills_and_project_matrix.md'
    with open(file_and_path, 'r', encoding='utf-8') as file:
        full_file = file.read()
   
    
    old_skills_overview_json = helpers.markdown_to_json(full_file)
    data = json.loads(old_skills_overview_json)
	
    #2) perform a search to create a record - write the file path to the json object we just got
	
    #'search' function code. We need save_path, name, and results
    if search_type == 'code':
        results = helpers.search_term(search, repo_path)
    if search_type == 'file':
        results = helpers.search_files(search, repo_path)
    if results:
        #TODO: For long files show short list.
        print(str(len(results)) + ' records found. First record below.')
        print(json.dumps(results[0],indent=4))
    else:
        print('No results found, change search paramaters.')
    #TODO fix this
    name = search
    save_path = helpers.record_struct(name,search,results)
    print('Record Recorded at '+save_path)

    #build relative path from src to ../../rubic/{language}/{file_name}
    example_str = "[" + name + "]" + "(../.." + save_path + ")" "<ul><li>Records found: " + str(len(results)) + "</li></ul>"
    
    print(example_str)

    #write in new data 
    for row in data:
        if row != '{}' and len(row) > 3: #ensure we're not in the empty row
            #put in 'Try / Except' block to prevent crash on bad user input
            #also - normalize for letter casing
            try:
                if row['category_name'] == category and row['subcategory_name'] == subcat: #ensure we write the correct cell
                    print(row['example'])
                    row['example'] = row['example'] + "<br>" + example_str
                    #TODO - don't overwrite the entire 'example' cell! Just append.
            except:
                print("Error - category name or sub-category name not defined. Ensure spelling is correct.")

    markdown = helpers.json_to_markdown_table(data)
    helpers.open_write('../assessments/user/overview_skills_and_project_matrix.md', markdown)

    return


#python src/cli/main.py build-project-assessment TwilioAITRust
#python src/cli/main.py build-project-assessment OpenSSF_Standards_Passing
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

#python src/cli/main.py search README --repo-path=Your/Cool/Repo --search-type=file
#python src/cli/main.py search 'README*' --search-type=file
#python src/cli/main.py search 'README*' --search-type=file -save
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