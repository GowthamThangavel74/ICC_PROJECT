from flask import Flask
from datetime import datetime
import re
from flask import render_template
import os

app = Flask(__name__)

Strings="Search Job"
Job_Des="Details"
Apply="Applied"
List=["1.Search Job", "2.Details","3.Applied"]
LIst = []

@app.route("/")
def home(name="Yes"):
        return render_template(
            "hello_there.html",
            name=name,
            LS=List
    )

@app.route("/")
def layout(name="Yes"):
    print('List of job openings');
    file_name = os.getcwd();
    file = open(file_name + '\\' +'Job_list.txt', "r");
    for line in file:
        #print(line)
        LIst.append(line);
    return render_template(
        "layout.html",
        name=name,
        lay=Apply
    )
