import requests

def get_questions():
    res=requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow').json()
    return res['items']
