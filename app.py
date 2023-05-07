from __future__ import unicode_literals
from flask import Flask, render_template, request, send_file
from pytube import YouTube
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def dl():
    if request.method == 'POST':
        url = request.form["url"]
        ACCESS_TOKEN = ""

        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

        data = {
            "message": url
        }

        requests.post(
            "https://notify-api.line.me/api/notify",
            headers=headers,
            data=data,
        )

        yt = YouTube(url).streams.get_highest_resolution().download()
        print(yt)
        fname = yt.split('//')[-1]
        return send_file(fname, as_attachment=True)

    else:
        return render_template('index.html')


if __name__ == "__main__":

    app.run()
