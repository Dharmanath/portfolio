from flask import Flask
from flask import Blueprint, render_template,send_from_directory,request,flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('ec_projects.html')

@app.route('/ec_projects')
def ec_projects():
    return render_template('ec_projects.html')

@app.route('/js_projects')
def js_projects():
    return render_template('js_projects.html')

@app.route('/re_projects')
def re_projects():
    return render_template('re_projects.html')

@app.route('/en_projects')
def en_projects():
    return render_template('en_projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/personal_css/<path:path>')
def personal_css(path):
    return send_from_directory('personal_css', path)

@app.route('/personal_images/<path:path>')
def personal_images(path):
    return send_from_directory('personal_images', path)

@app.route('/blogs_images/<path:path>')
def blogs_images(path):
    return send_from_directory('blogs_images', path)

@app.route('/personal_js/<path:path>')
def personal_js(path):
    return send_from_directory('personal_js', path)

@app.route('/fonts/<path:path>')
def personal_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/personal_data/<path:path>')
def personal_data(path):
    return send_from_directory('personal_data', path)

@app.route('/blogs/<path:path>')
def blog_data(path):
    return send_from_directory('blogs', path)

@app.route('/vision')
def vision():
    return render_template('VISION.html')

@app.route('/robots.txt')
def send_report():
    return send_from_directory('personal_data', "robots.txt")

@app.route('/sitemap.xml')
def send_xml():
    return send_from_directory('personal_data', "sitemap.xml")