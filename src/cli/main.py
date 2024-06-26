import json
import typer

import os
from pathlib import Path

from typing import Optional

try:
    from cli import helpers
except:
    import helpers

import importlib.resources as pkg_resources

from cli import templates

import json

app = typer.Typer(no_args_is_help=True)
environment = os.getenv('FLEDGER_ENVIRONMENT','production')

@app.command()
def getting_started(name: str):
    "Getting Started"
    print(
        f"Hello! Welcome to fledger! To get started read the README for a list of example and connect with the project at https://github.com/jasonburt/fledger."
    )

#test alias
#alias bfledger='python src/cli/main.py'

# python cli/main.py build-skill-assessment OpenSSF
# python cli/main.py build-skill-assessment OpenSSF --skills='documentation, reliability, efficiency, bug reports, and performance of products, software, bug report'
@app.command()
def build_skill_assessment(name: str, skills: str = ''):
    "Builds skill assessment using standards passed."
    print(f"Building {name} assesment in /assessment/user folder")
    # TODO standards index
    # Open Standards
    if environment == 'production':
        file_and_path_string = "standards/" + name + ".json"
    else:
        file_and_path_string = "src/tests/data/" + name + ".json"

    # file_and_path = Path("tests/data") / f"{name}.json"
    file_and_path = Path(file_and_path_string)
    skill_matrix_overview_path = "cli/templates/skill_matrix_overview.md" 


    # Convert to markdown
    try:
        with open(file_and_path, "r", encoding="utf-8") as file:
            standards_json = json.load(file)
    except:
        print('FileNotFoundError:'+file_and_path_string)
        return
    # TODO: Discovery functions
    # print(standards_json)
    skills_assment_matrix = helpers.flatten_categories(standards_json)
    skills_assment_matrix = helpers.mixin_skill_assessment_details(
        skills_assment_matrix
    )
    try:
        with open(skill_matrix_overview_path, "r") as overview_file:
            skill_matrix_overview = overview_file.read()
    except:
        skill_matrix_overview = pkg_resources.read_text(templates, "skill_matrix_overview.md")

    #'if' block to handle optional argument of job qualities/skills, which is used to filter down the master overview md file
    if skills != '':
        #print(f"You have provided the following skill list: {skills}")
        if 'and ' in skills:
            skills = skills.replace('and ', '')
            skill_list = skills.split(", ") 
        skills_assment_matrix = helpers.trim_document_by_terms(skills_assment_matrix, skill_list)
    
    markdown = skill_matrix_overview
    markdown = markdown + " \n" + helpers.json_to_markdown_table(skills_assment_matrix)
    #print(markdown)
    helpers.open_write(
        Path("assessments/user/overview_skills_and_project_matrix.md"), markdown
    )
    print("Build Complete")


# python cli/main.py update-skill-assessment user 
#  (updates skill assessment in user folder)
"""
This function searches the /{folder} for the overview_skills_and_project_matrix.md file to be updated.
It scans the '/assessments/user/evidence.json' file to apply existing records to the appropriate 'example'
cell in the .md file, based on the record's Category and Sub-Category values. Records without these values
are dumped into the 'Uncategorized' category (not yet created)
"""
@app.command()
def update_skill_assessment(folder: str):
    "Updates skill assessment using standards passed."

    # routes are currently relative to src execution
    overview_and_path = "./assessments/user/overview_skills_and_project_matrix.md"
    evidence_and_path = "./assessments/user/evidence.json"

    # try to open ../assessments/user/overview_skills_and_project_matrix.md
    try:
        overview_file = open(overview_and_path, "r", encoding="utf-8")
        overview_full_file = overview_file.read()
        overview_file.close()
    except:
        print(f"Error: path '{overview_and_path}' is not a valid path.")

    # try to open ./assessments/project/evidence.json
    try:
        evidence_file = open(evidence_and_path, "r", encoding="utf-8")
        evidence_full_file = evidence_file.read()
        #print(evidence_full_file)
        evidence_file.close()
    except:
        print(f"Error: path '{evidence_and_path}' is not a valid path.")

    # collect the relevant records for updating

    #collect the text before and after the md table for preservation
    table_start = overview_full_file.index('|')
    table_end = overview_full_file.rfind('|')
    pre_table_str = overview_full_file[:table_start]
    post_table_str = overview_full_file[table_end:]
    overview_full_file = overview_full_file[table_start:table_end]
    
    old_skills_overview_json = helpers.markdown_to_json(overview_full_file)
    full_evidence_json = json.loads(evidence_full_file)
    uncat_str = ""

    for record in full_evidence_json:
        found = False
        # print(record)
        for row in old_skills_overview_json:
            try:
                #print(f"Record: {record['category']} -- {record['subcategory']}")
                #print(f"Row: {row['category_name']} -- {row['subcategory_name']}")
                if (
                    record["category"] == row["Category"]
                    and record["subcategory"] == row["Subcategory"]
                ):
                    # need line number of top of 'record'. Verify this functionality as the evidence file grows.
                    line_number = helpers.find_line_number(
                        record["pattern"], evidence_and_path
                    )
                    example_str = (
                        "["
                        + record["pattern"]
                        + "]"
                        + "("
                        + "evidence.json" #changing from 'evidence_and_path' var to fix pathing
                        + "#L="
                        + str(line_number)
                        + ")"
                        "<ul><li>Records found: "
                        + str(len(record["records"]))
                        + "</li></ul>"
                    )
                    row["example"] = example_str
                    found = True
            except:
                pass  # handles the potentially empty rows at the end of overview_skills_and_project.md. No need to alert the user.
        if found is False:
            # here, we assign the record to the "uncategorized" area of the md
            line_number = helpers.find_line_number(record["pattern"], evidence_and_path)
            uncat_str = (
                uncat_str
                + "["
                + record["pattern"]
                + "]"
                + "(../."
                + evidence_and_path
                + "#l{line_number})"
                "<ul><li>Records found: "
                + str(len(record["records"]))
                + "</li></ul><br>"
            )

    # TODO - verify this functionaltiy once the 'Uncategorized' row is created
    found = False
    for row in old_skills_overview_json:
        try:
            if row["category_name"] == "Uncategorized":
                row["example"] = uncat_str
                found = True
        except:
            pass  # handles the empty rows at the end of overview_skills_and_project.md. No need to alert the user.
    if found is False:
        print(
            "Notice - the category 'Uncategorized' does not exist yet, or the name does not match."
        )

    markdown = helpers.json_to_markdown_table(old_skills_overview_json)
    markdown = pre_table_str + markdown + post_table_str 
    helpers.open_write(
        Path("./assessments/user/overview_skills_and_project_matrix.md"), markdown
    )

    return

# python cli/main.py build-project-assessment TwilioAITRust
# python cli/main.py build-project-assessment OpenSSF
# python src/cli/main.py search 'README*' --search-type=file --save=project --category=Basics --subcategory=Documentation
@app.command()
def build_project_assessment(name: str):
    "Builds repo standards assessment in the standards file."

    print(f"Building {name} assesment in /assessment/project folder")
    # Open Standards
    if environment == 'production':
        file_and_path_string = "standards/" + name + ".json"
    else:
        file_and_path_string = "src/tests/data/" + name + ".json"
    #print(f"Building Standards in /assessments/project folder {name}")
    # Open Standards
    file_and_path = Path(file_and_path_string)
    skill_matrix_overview_path = "cli/templates/project_matrix_overview.md" 

    # Convert to markdown
    try:
        with open(file_and_path, "r", encoding="utf-8") as file:
            standards_json = json.load(file)
    except:
        print(f"FileNotFoundError: {file_and_path}")
        return
    project_assment_matrix = helpers.flatten_categories(standards_json)
    project_assessment_matrix = helpers.mixin_project_assessment_details(
        project_assment_matrix
    )
    # TODO: Discovery functions
    try:
        with open(project_matrix_overview_path, "r") as overview_file:
            project_matrix_overview = overview_file.read()
    except:
        project_matrix_overview = pkg_resources.read_text(templates, "project_matrix_overview.md")
    markdown = project_matrix_overview
    markdown = markdown + " \n" +helpers.json_to_markdown_table(project_assessment_matrix)
    # print(markdown)
    helpers.open_write(Path("assessments/project/overview_project_matrix.md"), markdown)

# python cli/main.py update-project-assessment 
#  (updates skill assessment in user folder)
"""
This function searches the /{folder} for the overview_skills_and_project_matrix.md file to be updated.
It scans the '/assessments/user/evidence.json' file to apply existing records to the appropriate 'example'
cell in the .md file, based on the record's Category and Sub-Category values. Records without these values
are dumped into the 'Uncategorized' category (not yet created)
"""
@app.command()
def update_project_assessment(folder: str = ""):
    "Updates project assessment"

    # routes are currently relative to src execution
    overview_and_path = "assessments/project/overview_project_matrix.md"
    evidence_and_path = "assessments/project/evidence.json"

    # try to open ../assessments/user/overview_skills_and_project_matrix.md
    try:
        overview_file = open(Path(overview_and_path), "r", encoding="utf-8")
        overview_full_file = overview_file.read()
        overview_file.close()
    except:
        print(f"FileNotFoundError: '{overview_and_path}'")

    # try to open ./assessments/project/evidence.json
    try:
        evidence_file = open(evidence_and_path, "r", encoding="utf-8")
        evidence_full_file = evidence_file.read()
        #print(evidence_full_file)
        evidence_file.close()
    except:
        print(f"FileNotFoundError:'{evidence_and_path}'.")

    # collect the relevant records for updating

    #collect the text before and after the md table for preservation
    table_start = overview_full_file.index('|')
    table_end = overview_full_file.rfind('|')
    pre_table_str = overview_full_file[:table_start]
    post_table_str = overview_full_file[table_end:]
    overview_full_file = overview_full_file[table_start:table_end]
    
    old_skills_overview_json = helpers.markdown_to_json(overview_full_file)
    full_evidence_json = json.loads(evidence_full_file)
    uncat_str = ""

    for record in full_evidence_json:
        found = False
        # print(record)
        for row in old_skills_overview_json:
            try:
                #print(f"Record: {record['category']} -- {record['subcategory']}")
                #print(f"Row: {row['category_name']} -- {row['subcategory_name']}")
                if (
                    record["category"] == row["Category"]
                    and record["subcategory"] == row["Subcategory"]
                ):
                    # need line number of top of 'record'. Verify this functionality as the evidence file grows.
                    line_number = helpers.find_line_number(
                        record["pattern"], evidence_and_path
                    )
                    example_str = (
                        "["
                        + record["pattern"]
                        + "]"
                        + "("
                        + "evidence.json" #changing from 'evidence_and_path' var to fix pathing
                        + "#L="
                        + str(line_number)
                        + ")"
                        "<ul><li>Records found: "
                        + str(len(record["records"]))
                        + "</li></ul>"
                    )
                    row["example"] = example_str
                    found = True
            except:
                pass  # handles the potentially empty rows at the end of overview_skills_and_project.md. No need to alert the user.
        if found is False:
            # here, we assign the record to the "uncategorized" area of the md
            line_number = helpers.find_line_number(record["pattern"], evidence_and_path)
            uncat_str = (
                uncat_str
                + "["
                + record["pattern"]
                + "]"
                + "(../."
                + evidence_and_path
                + "#l{line_number})"
                "<ul><li>Records found: "
                + str(len(record["records"]))
                + "</li></ul><br>"
            )

    # TODO - verify this functionaltiy once the 'Uncategorized' row is created
    found = False
    for row in old_skills_overview_json:
        try:
            if row["category_name"] == "Uncategorized":
                row["example"] = uncat_str
                found = True
        except:
            pass  # handles the empty rows at the end of overview_skills_and_project.md. No need to alert the user.
    if found is False:
        print(
            "Notice - the category 'Uncategorized' does not exist yet, or the name does not match."
        )

    markdown = helpers.json_to_markdown_table(old_skills_overview_json)
    markdown = pre_table_str + markdown + post_table_str 
    helpers.open_write(
        Path("./assessments/project/overview_project_matrix.md"), markdown
    )

    return


# python cli/main.py search 'README' --repo-path=Your/Cool/Repo --search-type=file
# python cli/main.py search 'README*' --search-type=file
# python cli/main.py search 'README*' --search-type=file --save
# python cli/main.py search 'README*' --search-type=file --save=user --category=Basics --subcategory=Documentation
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
        print("No results found, change search parameters.")
    if save != "":
        # TODO fix this
        name = search
        helpers.record_struct(
            name, search, search_type, results, save, category, subcategory
        )


if __name__ == "__main__":
    app()
