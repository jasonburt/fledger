import pytest
import subprocess

# Basic Snapshot Test for high level commands
# More info on Typer Testing https://typer.tiangolo.com/tutorial/testing/
# run from the /src folder
# python -m pytest
from typer.testing import CliRunner
from ..cli.main import app
from ..cli import helpers

runner = CliRunner()


def test_command_search_file():
    # python src/cli/main.py search "README*" --search-type=file
    result = runner.invoke(app, ["search", "README*", "--search-type=file"])
    assert "records found. First record below." in result.stdout
    assert '"path_and_file": "README.md"' in result.stdout


def test_command_search_code():
    # python src/cli/main.py search "README*" --search-type=file
    result = runner.invoke(app, ["search", "import", "--search-type=code"])
    assert "records found. First record below." in result.stdout
    assert '"path_and_file": "cli/helpers.py' in result.stdout


def test_command_build_skill_assesment():
    # python src/cli/main.py build-skill-assessment OpenSSF_Standards_Passing
    result = runner.invoke(app, ["build-skill-assessment", "OpenSSF_Standards_Passing"])
    assert (
        "Building Standards in /standards folder OpenSSF_Standards_Passing"
        in result.stdout
    )
    #  TODO:Check file for this
    # assert "'category_name': 'Basics'" in result.stdout


def test_update_skill_assessment():
    # python src/cli/main.py update-skill-assessment user
    overview_and_path = "../assessments/user/overview_skills_and_project_matrix.md"
    result = runner.invoke(app, ["update-skill-assessment", "user"])

    try:
        overview_file = open(overview_and_path, "r", encoding="utf-8")
        overview_full_file = overview_file.read()
        overview_file.close()
    except:
        print(f"Error: path '{overview_and_path}' is not a valid path.")
    assert "README*" in overview_full_file

    # row check - ensure we didn't break the rows
    # check the first and the last row to ensure

    assert "Error" not in result.stdout
    
def test_build_job_assessment():
    # python src/cli/main.py build-job-assessment OpenSSF_Standards_Passing
    overview_and_path = "./assessments/user/job_reqs_matrix.md"
    result = runner.invoke(app, ["build-job-assessment", "OpenSSF_Standards_Passing", "documentation, reliability, efficiency, bug reports, and performance of products"])
    assert (
        "Building Job Requirements in /standards folder OpenSSF_Standards_Passing"
        in result.stdout
    )
    try:
        job_file = open(overview_and_path, "r", encoding="utf-8")
        job_full_file = job_file.read()
        job_file.close()
    except:
        print(f"Error: path '{overview_and_path}' is not a valid path.")
    assert "Term matched" in job_full_file
    
def test_update_job_assessment():
    overview_and_path = "./assessments/user/job_reqs_matrix.md"
    result = runner.invoke(app, ["update-job-assessment", "user"])

    try:
        overview_file = open(overview_and_path, "r", encoding="utf-8")
        overview_full_file = overview_file.read()
        overview_file.close()
    except:
        print(f"Error: path '{overview_and_path}' is not a valid path.")
    assert "README*" in overview_full_file

    # row check - ensure we didn't break the rows
    # check the first and the last row to ensure

    assert "Error" not in result.stdout
    
        
	
        
        
    
