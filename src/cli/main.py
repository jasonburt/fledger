import typer
from typing import Optional

try:
    from cli import helpers
except:
    import helpers


import json

app = typer.Typer(no_args_is_help=True)


@app.command()
def getting_started(name: str):
    "Getting Started"
    print(
        f"Hello! Welcome to fledger! To get started read the README for a list of example and connect with the project at https://github.com/jasonburt/fledger."
    )


# python cli/main.py build-skill-assessment OpenSSF_Standards_Passing
@app.command()
def build_skill_assessment(name: str):
    "Builds skill assessment using standards passed."
    print(f"Building Standards in /standards folder {name}")
    # TODO standards index
    # Open Standards
    file_and_path = "tests/data/" + name + ".json"

    # Convert to markdown
    with open(file_and_path, "r", encoding="utf-8") as file:
        standards_json = json.load(file)
    # TODO: Discovery functions
    # print(standards_json)
    skills_assment_matrix = helpers.flatten_categories(standards_json)
    skills_assment_matrix = helpers.mixin_skill_assessment_details(
        skills_assment_matrix
    )
    markdown = helpers.json_to_markdown_table(skills_assment_matrix)
    helpers.open_write(
        "/assessments/user/overview_skills_and_project_matrix.md", markdown
    )
    print("Build Complete")

    

#python cli/main.py update-skill-assessment user (updates skill assessment in user folder)
"""
This function searches the /user/evidence
/category/sub-category folder for records. Updates skill-assessment based on record 'type'
"""
@app.command()
def update_skill_assessment(folder: str):
    "Updates skill assessment using standards passed."
    col_index = 0
    letter_index = 0
    #print(f"Updating skill assessment in the {category}:{subcat} with {command}:{search}...")
    overview_and_path = '../assessments/user/overview_skills_and_project_matrix.md'
    evidence_and_path = "../assessments/user/evidence.json"

    #try to open ../assessments/user/overview_skills_and_project_matrix.md
    try:
        overview_file = open(overview_and_path, 'r', encoding='utf-8')
        overview_full_file = overview_file.read()
        overview_file.close()
    except:
        print(f"Error: path '{overview_and_path}' is not a valid path.")

    #try to open ./assessments/project/evidence.json
    try:
        evidence_file = open(evidence_and_path, 'r', encoding='utf-8')
        evidence_full_file = evidence_file.read()
        evidence_file.close()
    except:
        print(f"Error: path '{evidence_and_path}' is not a valid path.")

    
   
    #collect the relevant records for updating
    old_skills_overview_json = helpers.markdown_to_json(overview_full_file)
    full_evidence_json = json.loads(evidence_full_file)

    uncat_str = ""

    for record in full_evidence_json:
        found = False
        for row in old_skills_overview_json:
            try:
                if record['category'] == row['category_name'] and record['subcategory'] == row['subcategory_name']:
                    #need line number of top of 'record'
                    line_number = helpers.find_line_number(record['pattern'], evidence_and_path)
                    example_str = "[" + record['pattern'] + "]" + "(../." + evidence_and_path + "#l{line_number})" "<ul><li>Records found: " + str(len(record['records'])) + "</li></ul>"
                    row['example'] = example_str
                    found = True
            except:
                pass #handles the empty rows at the end of overview_skills_and_project.md. No need to alert the user.
        if found is False:
            #here, we assign the record to the "uncategorized" area of the md
            line_number = helpers.find_line_number(record['pattern'], evidence_and_path)
            uncat_str = uncat_str + "[" + record['pattern'] + "]" + "(../." + evidence_and_path + "#l{line_number})" "<ul><li>Records found: " + str(len(record['records'])) + "</li></ul><br>" 
            pass
            #

    found = False
    for row in old_skills_overview_json:
        try:
            if row['category_name'] == 'Uncategorized':
                row['example'] = uncat_str
                found = True
        except:
            pass #
    if found is False:
        print("Notice - the category 'Uncategorized' does not exist yet, or the name does not match.")

        
                
    markdown = helpers.json_to_markdown_table(old_skills_overview_json)
    helpers.open_write('../assessments/user/overview_skills_and_project_matrix.md', markdown)
    
    
    return




	

    # NOTE -- search has already been performed. update-skill-assessment scans record structs in /user/evidence.json and updates the 
    #         skills assessment based on the 'category', 'sub-category', and'type' tag in the record
    #         Assessments folder - we have src/assessments and /assessments. Do we need both? 
    #           A: just the highest level one 
    #
    #         In search, we create a record in evidence.json. When do we specify the category and subcategory for these
    #         records? Arguments to search? 
    #           A: If the records have unspecified categories, then we can list these records in a seperate area marked as such.
    #              We'll update the skill assessment with all tagged records, and we will update the 'untagged' records in their section.
    #
    #         When we update a skill assessment, we want to link to a json file in the 'examples' column to avoid
    #         pasting entire records in and cluttering the space. But are we still creating a json file for each individual
    #         record? 
    #           A: include '#l{line-number}' in the route to make an anchor link in evidence.json
            #more todo notes
            #Python 3.9.13 - current
            #python3.12.2 - needed 
	



# python cli/main.py build-project-assessment TwilioAITRust
# python cli/main.py build-project-assessment OpenSSF_Standards_Passing
@app.command()
def build_project_assessment(name: str):
    "Builds repo standards assessment in the standards file."
    print(f"Building Standards in /assments/project folder {name}")
    # Open Standards
    file_and_path = "tests/data/" + name + ".json"
    # Convert to markdown
    with open(file_and_path, "r", encoding="utf-8") as file:
        standards_json = json.load(file)
    project_assment_matrix = helpers.flatten_categories(standards_json)
    project_assessment_matrix = helpers.mixin_project_assessment_details(
        project_assment_matrix
    )
    # TODO: Discovery functions
    markdown = helpers.json_to_markdown_table(project_assessment_matrix)
    helpers.open_write("/assessments/project/overview_project_matrix.md", markdown)


# python cli/main.py search 'README' --repo-path=Your/Cool/Repo --search-type=file
# python cli/main.py search 'README*' --search-type=file
# python cli/main.py search 'README*' --search-type=file --save
# python cli/main.py search 'README*' --search-type=file --save=user Basic Documentation (?)
@app.command()
def search(
    search: str,
    repo_path: str = "",
    search_type: str = "code",
    save: str = "",
    category="",
    subcategory="",
):
    "Searches for a specific term in a repo."
    if search_type == "code":
        results = helpers.search_term(search, repo_path)
    if search_type == "file":
        results = helpers.search_files(search, repo_path)
    if results:
        # TODO: For long files show short list.
        print(str(len(results)) + " records found. First record below.")
        print(json.dumps(results[0], indent=4))
    else:
        print("No results found, change search paramaters.")
    if save != "":
        # TODO fix this
        name = search
        save_path = helpers.record_struct(
            name, search, search_type, results, save, category, subcategory
        )
        print("Record Recorded at " + save_path)


if __name__ == "__main__":
    app()
