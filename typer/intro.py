import typer
from typing import Optional

#create typer.typer() app
app = typer.Typer()


# Define a callback function to be executed before a command is invoked
@app.callback()
def before_command_callback():
    typer.echo("Before command, callback method is invoked first")

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}")

@app.command()
def greet(name: str = typer.Argument("world", help="The name to greet", show_default=True)):
    typer.echo(f"Hello, {name}!")

@app.command()
def backup(database: str, output_dir: str, force: bool = False):
    if force:
        typer.echo("Forced backup requested!")
    else:
        typer.echo("Regular backup Reqested!")
    typer.echo(f"Database: {database}")
    typer.echo(f"Output Directory: {output_dir}")

#def type_example(name: str, formal: bool = False, intro: Optional[str] = None):
 #   pass


#Typer app for files
files_app = typer.Typer(name="files", help="Manage files")





if __name__ == "__main__":
    app()
