from flask import Flask
from flask import request
from flask import render_template
from engine import track_url
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html',link="#")

@app.route("/",methods=['GET','POST'])
def home_post():
    url = request.form['url']
    down_link=get_track(url)
    return render_template('index.html',link=down_link)

 
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)
