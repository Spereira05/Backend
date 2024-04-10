import click

@click.group
def cli():
    pass

@cli.command()
def show():
    pass

@cli.command()
@click.argument("name")
def add(name:str):
    pass


if __name__ == "__main__":
    cli()
