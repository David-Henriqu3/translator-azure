import os
import requests
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv('TRANSLATOR_KEY')
if not KEY:
    raise RuntimeError("Chave de tradução não encontrada. Defina TRANSLATOR_KEY no arquivo .env ou variável de ambiente.")

ENDPOINT = os.getenv('TRANSLATOR_ENDPOINT', 'https://api.cognitive.microsofttranslator.com/')
LOCATION = os.getenv('TRANSLATOR_LOCATION', 'brazilsouth')

def traduzir(texto, para="pt"):
    url = ENDPOINT + "/translate"
    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Ocp-Apim-Subscription-Region': LOCATION,
        'Content-type': 'application/json'
    }
    params = {'api-version': '3.0', 'to': para}
    body = [{'text': texto}]
    response = requests.post(url, params=params, headers=headers, json=body)
    return response.json()[0]['translations'][0]['text']

def extrair_e_traduzir(url, seletor):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    conteudo = soup.select_one(seletor)
    
    if not conteudo:
        print(f"Seletor não encontrado!")
        return None
    
    markdown = []
    
    for tag in conteudo.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'blockquote']):
        texto = tag.get_text().strip()
        if not texto:
            continue
            
        texto_traduzido = traduzir(texto)
        
        if tag.name == 'h1':
            markdown.append(f"# {texto_traduzido}\n")
        elif tag.name == 'h2':
            markdown.append(f"## {texto_traduzido}\n")
        elif tag.name == 'h3':
            markdown.append(f"### {texto_traduzido}\n")
        elif tag.name == 'h4':
            markdown.append(f"#### {texto_traduzido}\n")
        elif tag.name == 'h5':
            markdown.append(f"##### {texto_traduzido}\n")
        elif tag.name == 'h6':
            markdown.append(f"###### {texto_traduzido}\n")
        elif tag.name == 'p':
            markdown.append(f"{texto_traduzido}\n")
        elif tag.name == 'li':
            markdown.append(f"- {texto_traduzido}\n")
        elif tag.name == 'blockquote':
            markdown.append(f"> {texto_traduzido}\n")
        
        time.sleep(0.1)
    
    return '\n'.join(markdown)

url = "https://dev.to/help/getting-started"
seletor = "#custom > div > div > div.tw-flex.tw-flex-col.md\\:tw-flex-row.tw-gap-8 > div"

conteudo = extrair_e_traduzir(url, seletor)

if conteudo:
    with open('conteudo_traduzido.md', 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print("Arquivo salvo!")
    print(conteudo[:300])