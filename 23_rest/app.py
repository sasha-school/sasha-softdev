import urllib.request
import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    with open("key_nasa.txt", "r") as file:
        key = file.read()
    data = urllib.request.urlopen(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    d = json.loads(data.read())
    return render_template('main.html', explanation = d["explanation"], imagehd = d["hdurl"], image = d["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
