import discord

from discord.message import Message

from eticgpt.clients import OllamaAPI
from eticgpt.models import OllamaPrompt
from eticgpt.models import OllamaResponse

intents = discord.Intents.default()

client = discord.Client(intents=intents)

ollamaAPI = OllamaAPI()

@client.event
async def on_connect():
    print(f'We connected as {client.user}')

@client.event
async def on_ready():
    print('We are ready')

@client.event
async def on_message(message: Message):
    assert message
    if message.author != client.user:
        if message.content.startswith('/ask'):
            question=OllamaPrompt(
                prompt=message.content.split('/ask')[-1]
            )
            response: OllamaResponse= ollamaAPI.prompt(prompt=question)

            if not response.done:
                await message.channel.send(':poop oops!')
            else:
                await message.channel.send(response.response)
            




