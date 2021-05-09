import urllib.request
import json
import os

def sendRequest(url):
    req = urllib.request.Request(url)
    req.headers = {
        'Authorization': 'Bearer ' + os.environ['TOKEN']
    }
    with urllib.request.urlopen(req) as response:
        decode = json.loads(response.read().decode('utf-8'))
    return decode

def getIds(url):
    decode = sendRequest(url)
    ids = []
    for s in range(len(decode)):
        ids.append(decode[s]['id'])
    return ids

def getViews(ids):
    originUrl = 'https://qiita.com/api/v2/items/'
    views = []
    for s in range(len(ids)):
        url = originUrl + ids[s]
        decode = sendRequest(url)
        views.append({
            "title": decode['title'],
            "views": decode['page_views_count']
        })
    
    return views

def views():
    url = 'https://qiita.com/api/v2/users/kiyo27/items?page=1&per_page=20'
    ids = getIds(url)
    return getViews(ids) 