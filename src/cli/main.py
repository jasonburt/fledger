import typer
from typing import Optional
import helpers
import json
import markdown_to_json

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


#python src/cli/main.py update-skill-assessment documentation detailed search README
@app.command()
def update_skill_assessment(category: str, subcat: str, command: str, term: str, repo_path: str=''):
    "Updates skill assessment using standards passed."
    col_index = 0
    letter_index = 0
    print(f"Updating section {category}:{subcat} with {command}:{term}...")
    file_and_path = 'assessments/user/overview_skills_and_project_matrix.md'
    with open(file_and_path, 'r', encoding='utf-8') as file:
        full_file = file.read()
   
    #store the existing skill assessment as a json file
    #need to delete this file when we're done
    helpers.mrkd2json(full_file, "assessments/user/tempSkillAssessment.json")

    #open our intermediary json input file, as well as our json output file
    infile = open("assessments/user/tempSkillAssessment.json", "r")

    data_file = infile.read()
    data = json.loads(data_file)
    new_data = helpers.search_term(term, repo_path)
 
    #evidence_str is the master list, which encompasses the entire 'example' cell
    evidence_str = "<ul>"
    key_str = ""
    record_count = 1

    #assemble the list of evidence in bullet point format
    for record in new_data:
         item_header_str = "<li>" + "Item " + str(record_count) + "<ul>"
         for key in record:
              key_str = key_str + "<li>" + key + "<ul>"
              content_str = "<li>" + str(record[key]) + "</li>"
              key_str = key_str + content_str + "</li></ul>"
         item_header_str = item_header_str + key_str + "</li></ul>"
         evidence_str = evidence_str + item_header_str
         record_count += 1
         key_str = ""
    evidence_str = evidence_str + "</ul>"

    #write in new data 
    for content in data:
        if content != '{}' and len(content) > 3: #ensure we're not in the empty row
            #put in 'Try / Except' block to prevent crash on bad user input
            #also - normalize for letter casing
            if content['Category'] == category and content['Sub Category'] == subcat: #ensure we write the correct cell
                content['example'] = evidence_str

    #convert our intermediary JSON data back to its proper .md file format
    markdown = helpers.json_to_markdown_table(data)
    helpers.open_write('assessments/user/tempSkillAssessmentUpdated.md', markdown)
    



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

#python src/cli/main.py search README --repo-path=Your/Cool/Repo
@app.command()
def search(search: str, repo_path: str = ''):
	"Searches for a specific term in a repo."
	results = helpers.search_term(search, repo_path)
	print(results)

if __name__ == "__main__":
	app()