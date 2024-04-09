import pytest
import subprocess

# Basic Snapshot Test for high level commands
#More info on Typer Testing https://typer.tiangolo.com/tutorial/testing/
# run from the /src folder
# python -m pytest
from typer.testing import CliRunner
from ..cli.main import app
runner = CliRunner()

def test_command_search_file():
	# python src/cli/main.py search "README*" --search-type=file
	result = runner.invoke(app, ["search", 'README*', "--search-type=file"])
	#     check = json.dumps( 
	# {
	#     "path_and_file": "README.md",
	#     "location": "",
	#     "code": "",
	#     "tags": [
	#         "build"
	#     ],
	#     "usage": "build"
	# })
	# print(result.stdout)
	assert 'records found. First record below.' in result.stdout
	assert '"path_and_file": "README.md"' in result.stdout

def test_command_search_code():
	# python src/cli/main.py search "README*" --search-type=file
	result = runner.invoke(app, ["search", 'import', "--search-type=code"])
	#     check = json.dumps( 
	# {
	#     "path_and_file": "README.md",
	#     "location": "",
	#     "code": "",
	#     "tags": [
	#         "build"
	#     ],
	#     "usage": "build"
	# })
	# print(result.stdout)
	assert 'records found. First record below.' in result.stdout
	assert '"path_and_file": "cli/helpers.py' in result.stdout