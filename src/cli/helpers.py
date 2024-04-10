import json, os, re
import subprocess


def check_project_settings():
    # Adding project settings over and over is a pain, so can we cconfigure with ENV or Setup file?
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

    # Create the table header
    markdown_table = "| " + " | ".join(headers) + " |\n"

    # Create the separator row
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Populate the table rows
    for item in data:
        row = "| " + " | ".join(str(item.get(header, "")) for header in headers) + " |"
        markdown_table += row + "\n"

    return markdown_table


def open_write(file_path, data):
    if "/" in file_path[0]:
        file_path = file_path[1:]
    folder_path = os.path.dirname(file_path)
    print(folder_path)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    f = open(file_path, "w")
    f.write(data)
    f.close()
    return file_path


def mixin_skill_assessment_details(standards_list):
    merge = {"language": "", "example": "", "rubric_notes": "", "general_notes": ""}
    for row in standards_list:
        print(row)
        row.update(merge)
    return standards_list


def mixin_project_assessment_details(standards_list):
    merge = {"language": "", "example": "", "rubric_notes": "", "general_notes": ""}
    for row in standards_list:
        print(row)
        row.update(merge)
    return standards_list


def flatten_categories(data):
    flattened = []
    for category in data["categories"]:
        for subcategory in category["subcategories"]:
            flattened_item = {
                "category_name": category["name"],
                "subcategory_name": subcategory["name"],
                "num_requirements": subcategory["numRequirements"],
                "requirements": subcategory["requirements"],
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
    save_path = "/assessments/" + save + "/evidence.json"
    # save_path = "/rubric/" + language + "/" + name + ".json"

    # Load records
    try:
        with open(save_path, "r") as records_file:
            records = json.loads(records_file)
    except:
        records = []
    record = {
        "name": name,
        "pattern": search,
        "type": search_type,
        "category": category,
        "subcategory": subcategory,
        "description": "",
        "records": [record_links],
    }
    records.append(record)
    save_records = json.dumps(records, indent=4)
    open_write(save_path, save_records)
    return save_path
