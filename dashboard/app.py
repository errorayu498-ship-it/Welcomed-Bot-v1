from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

CONFIG_FILE = "../config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE,"w") as f:
        json.dump(data,f,indent=4)

@app.route("/", methods=["GET","POST"])
def index():

    config = load_config()

    if request.method == "POST":

        config["welcome_channel"] = int(request.form["channel"])
        config["title"] = request.form["title"]
        config["subtitle"] = request.form["subtitle"]
        config["background_mode"] = request.form["background"]
        config["text_color"] = request.form["color"]

        save_config(config)

        return redirect("/")

    return render_template("index.html", config=config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)