# ========================================
# Bibliotecas
# ========================================
import requests

# ========================================
# Url da API
# ========================================
url = 'https://www.dnd5eapi.co/api/2014/'

# ========================================
# GET: Todas as classes
# ========================================
async def getClasses():
    # Pegando os dados
    response = requests.get(f'{url}classes/')
    # Tratando a resposta
    if response.status_code == 200:
        data  = response.json()
        names = [item['name'] for item in data['results']]
        return names
    else :
        return('Nenhum dado foi retornado.')
    
# ========================================
# GET: Todas as subclasses
# ========================================
async def getSubClasses():
    # Pegando os dados
    response = requests.get(f'{url}subclasses/')
    # Tratando a resposta
    if response.status_code == 200:
        data  = response.json()
        names = [item['name'] for item in data['results']]
        return names
    else :
        return('Nenhum dado foi retornado.')