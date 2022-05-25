import speech_recognition as sr
import pyttsx3
import requests 
from bs4 import BeautifulSoup
import webbrowser


def search(text):
    print('Googling...') # display text while downloading the Google page
    res = requests.get('https://google.com/search?q=' + ' '.join(text))
    res.raise_for_status()
    return res

def open_browser(search_for):
    s=search(search_for)
    soup = BeautifulSoup(s.text , "html.parser")

    linkElems = soup.select(' a ')
    numOpen = min(5, len(linkElems))
    webbrowser.open('https://google.com' + linkElems[2].get('href'))
  
