
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, jsonify
from historic_data_manager.historic_data_manager import Historic_Data_Manager
from database_manager.database_manager import Database_Manager


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

theDatabaseManager = Database_Manager()
my_historic_data_manager = Historic_Data_Manager(theDatabaseManager)
champions_data = my_historic_data_manager.obtainF1ChampionsData()
theDatabaseManager.storeF1ChampionsData(champions_data)