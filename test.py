import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os
import logging

# Configuration du bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('my_bot')

# Vérification de l'état du bot lorsqu'il est prêt
@bot.event
async def on_ready():
  logger.info(f'Connecté en tant que {bot.user.name}')

# Commande pour obtenir le statut de la lune
@bot.command(name='lune')
async def get_lunar_status(ctx):
  logger.info(f'Commande !lune exécutée par {ctx.author.name}')

  # Utilisez requests pour obtenir le contenu HTML de la page Web
  url = 'https://www.calendrier-lunaire.net/'
  response = requests.get(url)

  # Vérifiez si la requête HTTP a réussi
  if response.status_code == 200:
    logger.info('Requête HTTP réussie')

    # Utilisez BeautifulSoup pour analyser la page HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Recherchez l'élément HTML contenant les informations sur la lune
    lune_info = soup.find('div', {'class': 'mois_moon_full'})

    # Si l'élément est trouvé, extrayez le texte
    if lune_info:
      statut_lunaire = lune_info.get_text()
      logger.info('Statut lunaire récupéré avec succès')
    else:
      statut_lunaire = "Impossible de récupérer les informations sur la lune."
      logger.warning('Impossible de récupérer les informations sur la lune')
  else:
    statut_lunaire = "Impossible de se connecter au site Web."
    logger.error('Échec de la requête HTTP')

  # Envoyez le statut de la lune dans le canal Discord
  await ctx.send(statut_lunaire)

# Obtenez le token du bot à partir des variables d'environnement de Replit
my_secret = os.getenv('TOKEN')

# Assurez-vous que le bot est en ligne avec le bon token
bot.run(my_secret)


#bot.run('MTE1ODQ5OTI3MTY2NzA4OTQ4OA.GAI1d8.wsmfhLRDHxrMiFiRtgvquk3_dAHVkf6D-gDXtg')
