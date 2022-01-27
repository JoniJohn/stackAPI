import requests

def get_posts():
    res=requests.get('https://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow').json()
    return res['items']