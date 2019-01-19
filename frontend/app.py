import os
from flask import Flask, render_template, request, send_from_directory
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

APP_ROOT = os.path.dirname(__file__)

@app.route('/')
def index():
    onlyfiles = [f for f in listdir("videos") if isfile(join("videos", f))]
    return render_template('upload.html', videos=onlyfiles)

@app.route('/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'videos')
    file = request.files.getlist("file")[0]
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)

    return index()

@app.route('/getvideo/<path:path>')
def get_video(path):
    return send_from_directory('videos', path)

@app.route('/video/<id>')
def video(id):
    return render_template('video.html', id=id)

@app.route('/enhance/<id>')
def enhance(id):
    # Run the code to enhance the video
    return video(id)



if __name__=='__main__':
    app.run(debug=True)