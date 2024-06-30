import typer
from typing_extensions import Annotated
from typing import Optional
from wctool import __appName__,__version__
from pathlib import Path
import re
import os

app = typer.Typer()

def _version_callback(value : bool):
    if value:
        print(f'{__appName__} v{__version__}')
        raise typer.Exit()

def count_words(text:str) -> int:
    words : list[str] = re.findall(r'[^\s]+',text)
    return len(words)

def number_of_bytes(filename:str)->int:
    return os.stat(filename).st_size


@app.callback()
def main(version : Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help="Show application version and exit",
    callback=_version_callback,
    is_eager="true"
))-> None:
    return


@app.command()
def count(filename : Annotated[str,typer.Argument()],
          c : Annotated[bool, typer.Option(help="display number of bytes in a file")] = False,
          l : Annotated[bool, typer.Option(help="display number of lines in the file")] = False,
          m : Annotated[bool, typer.Option(help="display number of characters in the file")] = False
          ):
    try:
        if not(c or l or m):
            with open(filename,'r',encoding="utf8") as f:
                content = f.read()
                number_of_words = count_words(content)
                print(f'number of words in file are {number_of_words}')

        if l:
            with open(filename,'r',encoding='utf8') as f:
                print(len(f.readlines()))
        if c:
             print(number_of_bytes(filename))
        if m:
             print(number_of_bytes(filename))             
    except FileNotFoundError:
            print(f'file {filename} not found')
    except Exception as e:
            typer.echo(f"An error occurred: {str(e)}", err=True)    