import requests
from bs4 import BeautifulSoup
import pandas as pd

N = 3


def add_to_n(mnemonics_list, n):
    for i in range(n - len(mnemonics_list)):
        mnemonics_list.append('')
    return mnemonics_list


base_url = 'https://mnemonicdictionary.com/?word='

words = ('OBSCURANTISM', 'OBSEQUIOUS', 'OBSTREPEROUS')
data = list()

for word in words:
    url = base_url + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    slide = soup.find('div', class_='mnemonics-slides')
    cards = slide.find_all('div', class_='card-text')
    print(word)
    mnemonics = list()
    for card in cards[-N:]:
        mnemonics.append(card.find_all('p')[-1].text[1:-1])
    mnemonics = add_to_n(mnemonics, N)
    row = [word]
    row.extend(mnemonics)
    data.append(row)
    print(mnemonics)

pd.DataFrame(data, columns=['Word', '1st mnemonic', '2nd mnemonic', '3rd mnemonic']).to_csv('result.csv')