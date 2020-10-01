import requests
import json

def get_track(url):
    try:
        data=requests.get("https://api.soundcloud.com/resolve.json?url="+url+"&client_id=a3dd183a357fcff9a6943c0d65664087").json()
        track_id=str(data['id']) 
        data=requests.get("http://api.soundcloud.com/i1/tracks/"+track_id+"/streams?client_id=a3dd183a357fcff9a6943c0d65664087").json()
        mp3=data['http_mp3_128_url']
        return str(mp3)
    except Exception as e:
        print(str(e))
        return("Error!")
