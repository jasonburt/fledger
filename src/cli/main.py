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


#python src/cli/main.py update-project-assessment documentation detailed search README
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
    helpers.mrkd2json(full_file, "assessments/user/tempSkillAssessment.json")

    #open our intermediary json input file, as well as our json output file
    infile = open("assessments/user/tempSkillAssessment.json", "r")
    outfile = open("assessments/user/tempSkillAssessmentUpdated.json", "w")

    data_file = infile.read()
    data = json.loads(data_file)
    new_data = helpers.search_term(term, repo_path)
 
    evidence_str = ""
    evidence_count = 1

    #build the file directory for the evidence gathered 
    for item in new_data:
        evidence_str += "\n|- Item " + str(evidence_count)
        evidence_count += 1
        evidence_str = evidence_str + "\n|- - "
        for key in item:
            evidence_str = evidence_str + "\n|- - " + key
            evidence_str = evidence_str + "\n|- - - " + str(item[key])
            #print(f"Key: {key}, Value: {item[key]}")
    #print(evidence_str)

    #write in new data 
    for content in data:
        if content != '{}' and len(content) > 3:
            print(evidence_str)
            content['example'] = "hello :)"
            #the below method is not currently writing to the md file for some reason. It simply leaves content['example'] as blank
            #content['example'] = evidence_str 

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