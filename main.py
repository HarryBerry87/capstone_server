from flask import Flask, render_template, request, url_for
import os

PICTURE_FOLDER = os.path.join('static', 'pictures')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'mark.jpg')
    return render_template("index.html", user_image = full_filename)
