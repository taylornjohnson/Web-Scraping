from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask
app = Flask(__name__)

# Establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_mongo_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_mongo_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    #run the scrape function
    mars = scrape_mars.scrape_mars()
    mongo.db.collection.update({}, mars, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
