import json, os

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

def open_write(file_path,data):
    if '/' in file_path[0]:
        file_path = file_path[1:]
    folder_path = os.path.dirname(file_path)
    print(folder_path)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    f = open(file_path, "w")
    f.write(data)
    f.close()
    return file_path

def mixin_skill_assesment_details(standards_list):
    merge = {'language':'','example':'','notes':''}
    for row in standards_list:
        print(row)
        row.update(merge)
    return standards_list

def mixin_project_assesment_details(standards_list):
    merge = {'language':'','example':'','notes':''}
    for row in standards_list:
        print(row)
        row.update(merge)
    return standards_list

def flatten_categories(data):
    flattened = []
    for category in data['categories']:
        for subcategory in category['subcategories']:
            flattened_item = {
                'category_name': category['name'],
                'subcategory_name': subcategory['name'],
                'num_requirements': subcategory['numRequirements'],
                'requirements': subcategory['requirements']
            }
            flattened.append(flattened_item)
    return flattened
