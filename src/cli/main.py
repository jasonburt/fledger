import typer
from typing import Optional

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello(name: str):
    "Connect with the project at .... url."
    print(f"Hello {name}")

@app.command()
def build_standards(name: str):
    "Builds standards in /standards file."
    print(f"Building Standards in /standards folder {name}")

if __name__ == "__main__":
	app()