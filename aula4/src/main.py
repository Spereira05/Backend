import sys
import click


@click.command()
@click.argument('name')
def name(name:str):
        return click.echo(f"Hi, {name}!")

if __name__ == "__main__":
    name = sys.argv[1]
    name(name=name)  

