#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, jsonify, redirect
from scrape_mars import scrape
import pymongo


# In[2]:


# create instance of Flask app
app = Flask(__name__)


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn) 
db = client.mars_db
collection = db.items


# In[4]:


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


# In[5]:


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




