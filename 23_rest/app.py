import urllib.request
import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    data = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=GfPzg9QpYqRT8NdZvAH31A8q4k1gDwSrf4GooB3q')
    d = json.loads(data.read())
    return render_template('main.html', explanation = d["explanation"], imagehd = d["hdurl"], image = d["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
