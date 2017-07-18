from flask import Flask,request,url_for,render_template,send_from_directory
import subprocess
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"]="static/adobe/"
app.config["TEMPLATES_AUTO_RELOAD"]=True

app.root_path="C:/Users/alex-wlezien/Desktop/Github Projects/Instant Adobe/"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form/<path:file>")
def form(file):

    return render_template("form.html",file=file)

@app.route("/about")
def about():

    return "about page"


@app.route("/downloads/<path:filename>", methods=['GET', 'POST'])
def download(filename):
    if(request.method=="POST"):

        app.logger.error("this is the post method of download")

        #replace_text = request.form["replace_text"]
        uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])

        app.logger.error("the uploads directory is: " + uploads)
        app.logger.error("filename: " + filename)
        return send_from_directory(directory=uploads, filename=filename+".aep")
