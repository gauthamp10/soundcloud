from flask import Flask
from flask import request, send_from_directory
from flask import render_template
from engine import *
app = Flask(__name__)


@app.route("/")
def home():
    down_link={'downlink':'tumblr'}
    return render_template('index.html',link="#")

@app.route("/",methods=['GET','POST'])
def home_post():
    url = request.form['url']
    down_link=get_track(url)
    return render_template('index.html',link=down_link)

@app.route("/soundcloud.pw/<artist>/<song>/")
def quick(artist,song):
    part= artist+'/'+song
    url='https://soundcloud.com/'+part
    print(url)
    down_link=get_track(url)
    return render_template('quick_down.html',link=down_link)
    
        



if __name__ == '__main__':
    app.run()