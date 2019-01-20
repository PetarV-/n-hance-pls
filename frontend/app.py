import os
import sys
import shutil
from flask import Flask, render_template, request, send_from_directory
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

APP_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(APP_ROOT, '../'))

from backend.get_frames import video_to_frames, frames_to_video
from backend.nhancer import nhance

@app.route('/')
def index():
    onlyfiles = [f for f in listdir("frontend/videos") if isfile(join("frontend/videos", f))]
    return render_template('upload.html', videos=onlyfiles)

@app.route('/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'originals')
    file = request.files.getlist("file")[0]
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    _ = set_original(filename)

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
    src = os.path.join(APP_ROOT, 'originals')
    dst = os.path.join(APP_ROOT, 'videos')
    source = "/".join([src, path])
    destination = "/".join([dst, path])
    shutil.copy(source, destination)

    return index()

@app.route('/setenh/<path:path>')
def set_enhanced(path):
    src = os.path.join(APP_ROOT, 'enhanced')
    dst = os.path.join(APP_ROOT, 'videos')
    source = "/".join([src, path])
    destination = "/".join([dst, path])
    shutil.copy(source, destination)

    return index()

@app.route('download/<path:path>')
def download(path):
    return send_from_directory('enhanced', path)

@app.route('/video/<id>')
def video(id):
    return render_template('video.html', id=id)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
