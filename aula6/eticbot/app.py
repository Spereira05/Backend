import click

@click.group()
def bot():
    pass

@bot.command()
@click.option("-t", "--token")
def start(token:str):

    #discord.start()
    click.echo("hi from bot")

if __name__ == "__main__":
    bot(auto_envvar_prefix="ETIC")