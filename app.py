from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bson import Binary, Code
from bson.json_util import dumps
#import json
import craftapp


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craftapp"
mongo = PyMongo(app)
#reset the Mongo database
#mongo.db.collection.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find records of data from the mongo database
    beer_data = mongo.db.collection.find()
    #return(beer_data)
    # Return template and data
    return render_template("index.html", craft_info=beer_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    # Run the scrape function
    beer_data = craftapp.scrape_info()
    #print(beer_data)

    #reset the Mongo database
    mongo.db.collection.drop()
    mongo.db.collection.insert_many(beer_data)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)