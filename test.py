import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command()
async def lune(ctx):
    # Remplacez cette ligne par le code pour récupérer le statut de la lune à partir du site de calendrier lunaire
    statut_lunaire = "Le statut de la lune est : [insérez le statut ici]"
 
    await ctx.send(statut_lunaire)

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre propre bot
bot.run('YOUR_BOT_TOKEN')
