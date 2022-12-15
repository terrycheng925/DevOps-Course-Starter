from flask import Flask
from flask import render_template 
from flask import request, redirect, url_for 

from todo_app.flask_config import Config
from todo_app.data.session_items import *


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=["POST", "GET"])
def index():
    print(os.getenv('TRELLO_APITOKEN')
    items = get_items()

    if request.method == "POST":
        my_item = request.form["todo_item"] 
        print(my_item)
        items = add_item(my_item)
        return redirect('/')
    else:
    # items = get_items()
        return render_template("index.html", items=items)

