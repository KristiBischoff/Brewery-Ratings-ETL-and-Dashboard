from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bson import Binary, Code
from bson.json_util import dumps
#import json
import craftapp


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/craftapp")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    beer_data = dumps(mongo.db.collection.find())
    return(beer_data)

    # Return template and data
    return render_template("index.html", craft_info=beer_data)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    beer_data = craftapp.scrape_info()
    print(beer_data)

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.drop()
    mongo.db.collection.insert_many(beer_data)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)