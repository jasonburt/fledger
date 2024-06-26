import json
import os
import re
import subprocess
from pathlib import Path

environment = os.getenv('FLEDGER_ENVIRONMENT','production')

def check_project_settings():
    # Adding project settings over and over is a pain, so can we configure with ENV or Setup file?
    # Environment Variable
    repo_path = os.environ["fledger_project_path"]
    # Configuration
    return repo_path


def json_to_markdown_table(json_data):
    """
    Converts a JSON object to a Markdown table.

    Args:
    - json_data: A JSON object as a string or a Python list of dictionaries.

    Returns:
    - A string containing the Markdown representation of the table.
    """
    # Parse the JSON data if it's a string
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Check if the data is empty
    if not data:
        return "Empty data provided."

    # Extract headers
    headers = list(data[0].keys())
    #print("headers")
    #print(headers)

    # Create the table header
    markdown_table = "| " + " | ".join(headers) + " |\n"
    # Create the separator row
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    # Populate the table rows
    for item in data:
        # row = "| " + " | ".join(str(item.get(header, "")) for header in headers) + " |"
        row = "| "
        for header in headers:
            # Check for array
            value = item.get(header, "")
            if isinstance(value, list):
                value = "<br>".join(str(value_item) for value_item in value)
            value = str(value)
            if header != headers[-1]:
                row += value + " | "
            else:
                row += value
        markdown_table += row + "\n"

    return markdown_table


def open_write(file_path: Path, data):
    file_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"{file_path.name} was saved to {file_path.parent}")

    with open(file_path, "w") as f:
        f.write(data)


def mixin_skill_assessment_details(standards_list):
    merge = {"example": "", "notes": ""}
    for row in standards_list:
        row.update(merge)
    return standards_list


def mixin_project_assessment_details(standards_list):
    merge = { "example": "", "notes": ""}
    for row in standards_list:
        row.update(merge)
    return standards_list


def flatten_categories(data):
    flattened = []
    for category in data["categories"]:
        for subcategory in category["subcategories"]:
            flattened_item = {
                "Category": category["name"],
                "Subcategory": subcategory["name"],
                "Requirements": subcategory["requirements"],
            }
            flattened.append(flattened_item)
    return flattened


def search_files(term, repo_path):
    base_dir = os.getcwd()
    if repo_path and repo_path != "":
        base_dir = repo_path
    print("git ls-files " + term)
    process = subprocess.Popen(
        [
            "git",
            "ls-files",
            term,
        ],
        cwd=base_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    results_list = []
    results_clean_list = []
    while True:
        output = process.stdout.readline()
        try:
            results_list.append(output.strip().decode("utf-8"))
        except:
            print("failed append result")
            print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            # print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            # for output in process.stdout.readlines():
            #   print('last of output')
            #   print(output.strip())
            break
    for thing in results_list:
        if thing == "":
            continue
        item = {
            "path_and_file": thing,
            "location": "",
            "code": "",
            "tags": [],
            "usage": "",
        }
        if ".md" in item["path_and_file"]:
            item["tags"].append("build")
            item["usage"] = "build"
        results_clean_list.append(item)
    os.chdir(base_dir)
    return results_clean_list


def search_term(term, repo_path):
    base_dir = os.getcwd()
    print("git grep --text -n -f " + term)
    if repo_path and repo_path != "":
        base_dir = repo_path
    process = subprocess.Popen(
        [
            "git",
            "grep",
            "--text",
            "-n",
            term,
        ],
        cwd=base_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    results_list = []
    results_clean_list = []
    while True:
        output = process.stdout.readline()
        try:
            results_list.append(output.strip().decode("utf-8"))
        except:
            print("failed append result")
            print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            # print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            # for output in process.stdout.readlines():
            #   print('last of output')
            #   print(output.strip())
            break
    for thing in results_list:
        if "" == thing:
            continue
        path_and_file = thing.split(":")[0]
        location = thing.split(":")[1]
        sub_string = thing.replace(path_and_file + ":", "").replace(location + ":", "")
        # Good to see if its called somehow else here
        item = {
            "path_and_file": path_and_file,
            "location": location,
            "code": sub_string,
            "tags": [],
            "usage": "",
        }
        if "def" in item["code"]:
            item["tags"].append("build")
            item["usage"] = "build"
        if "=" in item["code"]:
            item["tags"].append("call")
            item["usage"] = "call"
        if "test" in item["path_and_file"]:
            item["tags"].append("test")
            item["usage"] = "test"
        results_clean_list.append(item)
    os.chdir(base_dir)
    return results_clean_list


def record_struct(name, search, search_type, record_links, save, category, subcategory):
    # Merge First
    original_records = []
    language = "general"
    name = re.sub("[^A-Za-z0-9]+", "", name)
    name = name + "_file_check"
    if environment == 'production':
        save_path = Path("assessments/"+save+"/evidence.json")
    else:
        print('running as dev')
        save_path = Path("assessments/"+save+"/evidence.json")
    
    # save_path = "/rubric/" + language + "/" + name + ".json"

    # Load records
    try:
        with open(save_path, "r")as records_file:
            records_data = records_file.read()
        records = json.loads(records_data)
        print(f"Existing Records: {len(records)}")
    except FileNotFoundError as fnf_errorr:
        print(f"FileNotFoundError:'{save_path}'.")

    

    
    record = {
        "name": name,
        "pattern": search,
        "type": search_type,
        "category": category,
        "subcategory": subcategory,
        "description": "",
        "records": [record_links],
    }
    if record in records:
        print(f"Existing Record, not updating")
    else:
        records.append(record)
        save_records = json.dumps(records, indent=4)
        open_write(save_path, save_records)
        print(f"Record Recorded to {save_path.parent}")
    return save_path


def markdown_to_json(inp):
    lines = inp.split("\n")
    ret = []
    keys = []
    for i, l in enumerate(lines):
        if i == 0:
            keys = [_i.strip() for _i in l.split("|")]
        elif i == 1:
            continue
        else:
            ret.append(
                {
                    keys[_i]: v.strip()
                    for _i, v in enumerate(l.split("|"))
                    if _i > 0 and _i < len(keys) - 1
                }
            )
    json_str = json.dumps(ret, indent=4)
    return json.loads(json_str)
    # print(mrkd2json(my_str))


def find_line_number(term: str, path: str):
    line_count = 0
    try:
        evidence_file = open(path, "r", encoding="utf-8")
        evidence_lines = evidence_file.readlines()
        evidence_file.close()
    except:
        print(f"Error: could not find evidence.json at '{path}'")
    for line in evidence_lines:
        # print(line)
        if term in line:
            return line_count
        else:
            line_count += 1
    if line_count == 0:
        print("Search term not found in given file.")
        return 0

def trim_document_by_terms(skills_matrix, skill_list):
    keep_row = False
    new_data = []
   
    for row in skills_matrix:
        keep_row = False
        for term in skill_list:
            if keep_row == True:
                break
            for sentence in row['Requirements']:
                if term in sentence:
                    row['notes'] = row['notes'] + "<ul><li>Term matched: **'" + term + "'**</li></ul>"
                    new_data.append(row)
                    keep_row = True
                    break
    return new_data