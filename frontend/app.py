import os
from flask import Flask, render_template, request, send_from_directory
from os import listdir
from os.path import isfile, join
from backend.get_frames import video_to_frames, frames_to_video
from backend.nhancer import nhance

app = Flask(__name__)

APP_ROOT = os.path.dirname(__file__)

@app.route('/')
def index():
    onlyfiles = [f for f in listdir("videos") if isfile(join("videos", f))]
    return render_template('upload.html', videos=onlyfiles)

@app.route('/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'originals')
    file = request.files.getlist("file")[0]
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    set_original(destination)

    return index()

@app.route('/getvideo/<path:path>')
def get_video(path):
    return send_from_directory('videos', path)

@app.route('/getorig/<path:path>')
def get_original(path):
    return send_from_directory('originals', path)

@app.route('/getenh/<path:path>')
def get_enhanced(path):
    return send_from_directory('enhanced', path)

@app.route('/getsplit/<path:path>')
def get_split(path):
    return send_from_directory('split', path)

@app.route('/setorig/<path:path>')
def set_original(path):
    file = send_from_directory('originals', path)
    target = os.path.join(APP_ROOT, 'videos')
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)

    return index()

@app.route('/setenh/<path:path>')
def set_enhanced(path):
    file = send_from_directory('enhanced', path)
    target = os.path.join(APP_ROOT, 'videos')
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)

    return index()

@app.route('/video/<id>')
def video(id):
    return render_template('video.html', id=id)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
