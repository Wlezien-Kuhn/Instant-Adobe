from flask import Flask,request,url_for,render_template,send_from_directory
import subprocess
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]="etdownloads/"
app.root_path="C:/Users/alex-wlezien/Desktop/Github Projects/Instant Adobe/"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form/")
def form():

    return "form page"

@app.route("/about")
def about():

    return "about page"


@app.route("/downloads/<path:filename>", methods=['GET', 'POST'])
def download(filename):
    if(request.method=="POST"):

        app.logger.error("this is the post method of download")

        replace_text = request.form["replace_text"]
        uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])

        app.logger.error("the uploads directory is: " + uploads)
        return send_from_directory(directory=uploads, filename=filename)
