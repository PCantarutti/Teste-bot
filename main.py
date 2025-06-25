# ========================================
# Bibliotecas
# ========================================
import os
import discord

# ========================================
# Módulos
# ========================================
from discord     import app_commands
from discord.ext import commands
from dotenv      import load_dotenv

# ========================================
# Pegando funções
# ========================================
from sistemas.dungeons_dragons import *
from dados.dices import *

# ========================================
# Carregando o ENV
# ========================================
load_dotenv()

# ========================================
# Criando variáveis
# ========================================
token   = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot     = commands.Bot('/', intents=intents)

# ========================================
# Evento de criação do bot
# ========================================
@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Bot iniciado com sucesso.')
    
# ========================================
# Criando os comandos
# ========================================
@bot.tree.command(description='Retorna informações sobre os comandos disponíveis.')
async def help(interact: discord.Interaction):
    await interact.response.send_message(
        '## 🤖| Comandos do Bot \n'
        '- /help \n'
        '- /ded  \n'
        '- /roll '
    )

@bot.tree.command(description='Retorna as informações do sistema D&D. Caso não saiba o que colocar, coloque `help` para saber mais.')
@app_commands.describe(informacao='O que deseja ver sobre o sistema. (inglês)')
async def ded(interact: discord.Interaction, informacao: str):
    match informacao:
        case 'help' :
            await interact.response.send_message(
                '## 🤖| Comandos disponíveis: \n'
                '- help \n'
                '- class \n'
                '- subclass \n'
                '** Obs: As informações da api serão retornadas em inglês **'
            )
        case 'class':
            await interact.response.send_message(f'As classes são: {await getClasses()}')
        case 'subclass':
            await interact.response.send_message(f'As classes são: {await getSubClasses()}')

@bot.tree.command(description='Retorna os valores de um rolamento de dados.')
@app_commands.describe(quantidade='Quantidade desejada de dados.', faces='Quantidade de faces do dado.(Ex: 6, 12, 20)')
async def roll(interact: discord.Interaction, quantidade: int, faces: int):
    # Tratativa de inputs
    if quantidade <= 0:
        await interact.response.send_message('🫏| Insira uma quantidade maior que zero para prosseguir.')
        return
    if quantidade > 20:
        await interact.response.send_message('🥵| Não é possível rolar mais de 20 dados por vez.')
        return
    # Rolando os dados
    await interact.response.send_message(f'🎲| Você rolou {quantidade}d{faces}: [{await girarDado(quantidade, faces)}]')
    

# ========================================
# Iniciando o bot
# ========================================
bot.run(token)