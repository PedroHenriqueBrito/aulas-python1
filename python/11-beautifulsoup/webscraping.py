import requests

from bs4 import BeautifulSoup

pagina = requests.get("https://quotes.toscrape.com/")

dadosPagina = BeautifulSoup(pagina.text, 'html.parser')

#(print(dadosPagina.prettify()))

#todasFrases = dadosPagina.find_all('div', class_ = "quote")

#for div in todasFrases:
#    print(div)

todasFrases = dadosPagina.find_all('span', itemprop = "text")

for span in todasFrases:
    print(span.text)