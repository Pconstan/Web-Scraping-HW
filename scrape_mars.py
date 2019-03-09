#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
import pandas as pd
import pymongo
from flask import Flask, render_template


# In[17]:


def init():
    executable_path = {'executable_path': 'C:\Program Files\Common Files\Chromedriver\chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)
    


# In[20]:


def scrape():
    browser = init()
    url_0 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url_0)
    
    for x in range(10):
        # HTML object
        html = browser.html
        # Parse HTML
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
        headlines = soup.find_all('div', class_='content_title')
        pgraph = soup.find_all('div', class_='article_teaser_body')
        
    ddd = headlines[0].find('a')
    news_title = ddd.contents[0]

    ppp = pgraph[0]
    news_p = ppp.contents[0]
    
    #JPL Mars Space Scrape
    url_1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find('article')
    
    gg = imgs.find('a')
    url_2 = gg['data-fancybox-href']
    featured_image_url = "https://www.jpl.nasa.gov" + url_2
    
        #Mars Weather Twitter Scrape
    url_3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_3)
    html = browser.html
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    m_weather = soup.find("div", class_="js-tweet-text-container")
    ss = m_weather.find('p')
    mars_weather = ss.contents[0]

    #Mars Facts Scrape
    url_4 = 'https://space-facts.com/mars/'
    browser.visit(url_4)
    
    tables = pd.read_html(url_4)
    
    df = tables[0]
    mars_facts = df.to_html()

    #Mars Hemispheres Scrape

    url1='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    url2='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    url3='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    url4='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    browser.visit(url1)
    html = browser.html
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    img1 = soup.find('img', class_='wide-image')
    h1 = 'https://astrogeology.usgs.gov' + img1['src']

    browser.visit(url2)
    html = browser.html
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    img2 = soup.find('img', class_='wide-image')
    h2 = 'https://astrogeology.usgs.gov' + img2['src']

    browser.visit(url3)
    html = browser.html
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    img3 = soup.find('img', class_='wide-image')
    h3 = 'https://astrogeology.usgs.gov' + img3['src']

    browser.visit(url4)
    html = browser.html
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    img4 = soup.find('img', class_='wide-image')
    h4 = 'https://astrogeology.usgs.gov' + img4['src']

    hemisphere_image_urls =  [{"title": "Valles Marineris Hemisphere", "img_url": h1},
        {"title": "Cerberus Hemisphere", "img_url": h2},
        {"title": "Schiaparelli Hemisphere", "img_url": h3},
        {"title": "Syrtis Major Hemisphere", "img_url": h4},
    ]


    mars_dict = {"news_title": news_title, "news_p": news_p, "featured_image_url": featured_image_url,
                  "mars_weather": mars_weather, "mars_facts":mars_facts, "hemisphere_image_urls": hemisphere_image_urls}
    
    return(mars_dict)


# In[21]:


scrape()


# In[ ]:




