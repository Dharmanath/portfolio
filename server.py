from flask import Flask
from flask import Blueprint, render_template,send_from_directory,request,flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/personal_css/<path:path>')
def personal_css(path):
    return send_from_directory('personal_css', path)

@app.route('/personal_images/<path:path>')
def personal_images(path):
    return send_from_directory('personal_images', path)

@app.route('/personal_js/<path:path>')
def personal_js(path):
    return send_from_directory('personal_js', path)

@app.route('/fonts/<path:path>')
def personal_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/personal_data/<path:path>')
def personal_data(path):
    return send_from_directory('personal_data', path)

@app.route('/vision')
def vision():
    return render_template('VISION.html')