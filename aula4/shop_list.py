import click
import os

# Initialize the shopping list from a file
def load_shopping_list(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the shopping list to a file
def save_shopping_list(file_name, shopping_list):
    with open(file_name, "w") as file:
        json.dump(shopping_list, file)

# Initialize the shopping list
shopping_list = load_shopping_list("shopping_list.json")

@click.group()
def cli():
    """A simple CLI shopping list"""
    pass

@cli.command("add")
@click.argument("item", required=True)
def add_item(item):
    """Add a new item to the shopping list"""
    if item in shopping_list:
        click.echo(f"{item} is already in the shopping list")
    else:
        shopping_list[item] = 1
        click.echo(f"{item} added to the shopping list")
        save_shopping_list("shopping_list.json", shopping_list)

@cli.command("increment")
@click.argument("item", required=True)
def increment_item(item):
    """Increment the quantity of an item in the shopping list"""
    if item in shopping_list:
        shopping_list[item] += 1
        click.echo(f"{item} quantity incremented")
        save_shopping_list("shopping_list.json", shopping_list)
    else:
        click.echo(f"{item} not found in the shopping list")

@cli.command("decrement")
@click.argument("item", required=True)
def decrement_item(item):
    """Decrement the quantity of an item in the shopping list"""
    if item in shopping_list:
        if shopping_list[item] > 0:
            shopping_list[item] -= 1
            click.echo(f"{item} quantity decremented")
            save_shopping_list("shopping_list.json", shopping_list)
        else:
            click.echo(f"{item} quantity already at 0")
    else:
        click.echo(f"{item} not found in the shopping list")

@cli.command("delete")
@click.argument("item", required=True)
def delete_item(item):
    """Delete an item from the shopping list"""
    if item in shopping_list:
        del shopping_list[item]
        click.echo(f"{item} deleted from the shopping list")
        save_shopping_list("shopping_list.json", shopping_list)
    else:
        click.echo(f"{item} not found in the shopping list")

@cli.command("list")
def list_items():
    """List all items in the shopping list"""
    if not shopping_list:
        click.echo("The shopping list is currently empty")
    else:
        for item, quantity in shopping_list.items():
            click.echo(f"{item}: {quantity}")

if __name__ == "__main__":
    cli()