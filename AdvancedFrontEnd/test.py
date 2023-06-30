import typer

app = typer.Typer()

@app.command()
def command1(arg: str):
    # Logic for command1
    response = f"Response1 for {arg}"
    typer.echo(response)

@app.command()
def command2(arg1: str, arg2: str, arg3: str):
    # Logic for command2
    response = f"Response2 for {arg1}, {arg2}, {arg3}"
    typer.echo(response)

def fake_cli():
    while True:
        command = input("> ")
        if command == "quit":
            break

        try:
            typer.main.get_command(app)(command.split()[1:])
        except (AttributeError, IndexError):
            typer.echo("Invalid command.")

if __name__ == "__main__":
    fake_cli()
