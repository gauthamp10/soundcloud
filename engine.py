import requests
import json

def get_track(url):
    try:
        data=requests.get("https://api.soundcloud.com/resolve.json?url="+url+"&client_id=FweeGBOOEOYJWLJN3oEyToGLKhmSz0I7").json()
        track_id=str(data['id'])
        track_title=str(data['title'])   
        data=requests.get("http://api.soundcloud.com/i1/tracks/"+track_id+"/streams?client_id=FweeGBOOEOYJWLJN3oEyToGLKhmSz0I7").json()
        mp3=data['http_mp3_128_url']
        return mp3
        

    except Exception as e:
        print(str(e))
        return("Error!")

