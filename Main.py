from flask import Flask,request,url_for,render_template,send_from_directory
import MySQLdb
import subprocess
import os
from . import db as dbhelper

app = Flask(__name__)

app.config["UPLOAD_FOLDER"]="static/adobe/"
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config['MYSQL_USER'] = 'adobe_test'
app.config['MYSQL_PASSWORD'] = 'instant_adobe'
app.config['MYSQL_DB'] = 'instant_adobe_data'
app.config['MYSQL_HOST'] = 'localhost'

app.root_path=os.path.dirname(os.path.realpath(__file__))

db = MySQLdb.connect(
                    host=app.config["MYSQL_HOST"],
                    user=app.config["MYSQL_USER"],
                    password=app.config["MYSQL_PASSWORD"],
                    db=app.config["MYSQL_DB"]
                )

@app.route("/")
def home():

    data = dbhelper.getAllTemplates(db.cursor())

    if data is None:
        app.logger.error("error accessing database in route /")
        return render_template("home.html",context={"error":"Problem with database query"})

    app.logger.error("route / : data = " + str(data))

    for row in data:

        app.logger.error(str(row))

    return render_template("home.html",data=data)

@app.route("/form/<unique_id>")
def form(unique_id):

    template = dbhelper.getTemplateWithUuid(db.cursor(),unique_id)

    return render_template("form.html",template=template)

@app.route("/about")
def about():

    return "about page"

@app.route("/shutdown")
def shutdown():

    shutdown_server()
    return "shutting down server..."


@app.route("/downloads/<path:filename>", methods=['GET', 'POST'])
def download(filename):
    if(request.method=="POST"):


        #replace_text = request.form["replace_text"]
        uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])

        app.logger.error("the uploads directory is: " + uploads)
        app.logger.error("filename: " + filename)

        return send_from_directory(directory=uploads, filename=filename+".aep")


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
