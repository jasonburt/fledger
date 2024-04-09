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
	assert 'records found. First record below.' in result.stdout
	assert '"path_and_file": "README.md"' in result.stdout

def test_command_search_code():
	# python src/cli/main.py search "README*" --search-type=file
	result = runner.invoke(app, ["search", 'import', "--search-type=code"])
	assert 'records found. First record below.' in result.stdout
	assert '"path_and_file": "cli/helpers.py' in result.stdout

def test_command_build_skill_assesment():
	# python src/cli/main.py build-skill-assessment OpenSSF_Standards_Passing
	result = runner.invoke(app, ["build-skill-assessment", 'OpenSSF_Standards_Passing'])
	assert 'Building Standards in /standards folder OpenSSF_Standards_Passing' in result.stdout
	assert "'standardsSet': 'OpenSSF Best Practices'" in result.stdout