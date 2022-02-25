import requests
from bs4 import BeautifulSoup
from datetime import date

wordleStartDate = date(2021, 6, 19)

try:
    html_text = requests.get('https://www.nytimes.com/games/wordle/index.html', headers={
        'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(html_text, 'lxml')
    hashText = 'window.wordle.hash'
    hash = soup.find_all('script')
    jsw = 'var Ma=['
    for script in hash:
        if hashText in str(script):
            hashStart = str(script).index(hashText)+len(hashText)+4
            hashEnd = str(script)[hashStart:].index("'")
            hashID = str(script)[hashStart:hashStart+hashEnd]

    if hashID:
        html_text = requests.get('https://www.nytimes.com/games/wordle/main.' + hashID + '.js', headers={
            'User-Agent': 'Mozilla/5.0'}).text

        soup = BeautifulSoup(html_text, 'lxml')
        wordleListStart = str(soup).index(jsw)+len(jsw)
        wordleListEnd = str(soup)[wordleListStart:].index(']')

        wordleList = list(
            str(soup)[wordleListStart:wordleListStart+wordleListEnd].replace('"', '').split(","))

        wordleIndex = date.today() - wordleStartDate
        wordle = wordleList[int(wordleIndex.days)]

    if wordle:
        print("Today's Wordle: {}".format(wordle))
    else:
        print("Something went wrong.")


except:
    print("Something went wrong.")
