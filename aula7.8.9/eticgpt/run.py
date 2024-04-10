import click
from eticgpt import bot as chat_bot

@click.group()
def bot():
    pass

@bot.command()
@click.Option('--token', show_envvar='BOT_TOKEN')
def start(token:str):
    chat_bot.client.run(token) 


if __name__ == "__main__":
    bot()
