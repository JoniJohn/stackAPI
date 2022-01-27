import requests

def get_articles():
    res=requests.get('https://api.stackexchange.com/2.3/articles?order=desc&sort=activity&site=stackoverflow').json()
    return res['items']