
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("Todays news are lets begin")
    url =  "https://newsapi.org/v2/top-headlines?country=us&apiKey=c011eb33d334490a917f6209174146d2"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news listen carefully")
    speak("thanks for listening")