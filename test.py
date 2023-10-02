import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command()
async def lune(ctx):
    # Utilisez requests pour obtenir le contenu HTML de la page Web
    url = 'https://www.calendrier-lunaire.net/'
    response = requests.get(url)
    
    # Vérifiez si la requête HTTP a réussi
    if response.status_code == 200:
        # Utilisez BeautifulSoup pour analyser la page HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Recherchez l'élément HTML contenant les informations sur la lune
        lune_info = soup.find('div', {'class': 'mois_moon_full'})
        
        # Si l'élément est trouvé, extrayez le texte
        if lune_info:
            statut_lunaire = lune_info.get_text()
        else:
            statut_lunaire = "Impossible de récupérer les informations sur la lune."
    else:
        statut_lunaire = "Impossible de se connecter au site Web."

    # Envoyez le statut de la lune dans le canal Discord
    await ctx.send(statut_lunaire)

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre propre bot
bot.run('MTE1ODQ5OTI3MTY2NzA4OTQ4OA.GAI1d8.wsmfhLRDHxrMiFiRtgvquk3_dAHVkf6D-gDXtg')
