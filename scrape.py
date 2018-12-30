

#Load Dependencies

from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd


def init_browser():
    executable_path = {'executable_path': r"\Users\marte\WASHSTL201809DATA3\chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'


    # Retrieve page with the requests module
    response = requests.get(url)


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')



    # Examine the results, then determine element that contains sought info
    print(soup.prettify())



    # Extract title text
    title = soup.find("div", class_="content_title").text
    print(title)


    # Print all paragraph texts
    paragraphs = soup.find("div", class_="rollover_description_inner").text

    print(paragraphs)




    #Visit Image URL

    url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)



    html = browser.html
    soup2= bs(html, 'html.parser')




    # Examine the results, then determine element that contains sought info
    print(soup2.prettify())




    soup2 = bs(html, 'html.parser')
    image = soup2.find("img", class_="thumb")["src"]

    print(image)



    url3 = 'https://www.jpl.nasa.gov'
    featured_image_url = url3 + image

    print(featured_image_url)




    url4 = 'https://twitter.com/marswxreport?lang=en'



    response_twitter = requests.get(url4)


    # Create BeautifulSoup object; parse with 'html.parser'
    twitter_soup = bs(response_twitter.text, 'html.parser')

    twitter_soup



    #prettify twitter soup
    print(twitter_soup.prettify())



    mars_weather = twitter_soup.find("div", class_="js-tweet-text-container").text

    print(mars_weather)



    url5 = 'http://space-facts.com/mars/'




    response_facts = requests.get(url5)


    facts_soup = bs(response_facts.text, 'html.parser')

    facts_soup



    mars_facts = facts_soup.find("table", class_="tablepress tablepress-id-mars").text

    fact_string = pd.read_html(response_facts.text)

    print(fact_string)


    type(fact_string)


    df = fact_string[0]
    df.set_index(0, inplace=True)
    df.columns = ['Facts']
    df




    html_df = df.to_html()

    html_df




    data_html = html_df.replace('\n', ' ')

    data_html



    url6 = 'http://web.archive.org/web/20181114182238/https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    usgs_browser = browser.visit(url6)


    response_usgs = requests.get(url6)




    usgs_soup = bs(response_usgs.text, 'html.parser')

    usgs_soup





    usgs_image = usgs_soup.find("img", class_="wide-image")["src"]
    main_url = "web.archive.org"
    cerebus_hem = main_url + usgs_image
    print(cerebus_hem)



    url7 = 'http://web.archive.org/web/20181114182242/https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    usgs2_browser = browser.visit(url7)



    response_usgs2 = requests.get(url7)


    usgs2_soup = bs(response_usgs2.text, 'html.parser')

    usgs2_soup



    usgs2_image = usgs2_soup.find("img", class_="wide-image")["src"]
    schiaparelli_hem = main_url + usgs2_image
    print(schiaparelli_hem)



    url8 = 'http://web.archive.org/web/20181114182245/https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    usgs3_browser = browser.visit(url8)



    response_usgs3 = requests.get(url8)

    usgs3_soup = bs(response_usgs3.text, 'html.parser')

    usgs3_soup


    usgs3_image = usgs3_soup.find("img", class_="wide-image")["src"]
    syrtis_hem = main_url + usgs3_image
    print(syrtis_hem)



    url9 = 'http://web.archive.org/web/20181114182248/https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    usgs4_browser = browser.visit(url9)


    response_usgs4 = requests.get(url9)


    usgs4_soup = bs(response_usgs4.text, 'html.parser')

    usgs4_soup


    usgs4_image = usgs4_soup.find("img", class_="wide-image")["src"]
    valles_hem = main_url + usgs_image
    print(valles_hem)


    hemisphere_list = [{"Title":'Valles', "image_url": valles_hem, "Title":"Syrtis", "image_url": syrtis_hem, "Title": "Schiaparelli", 
                   "image_url": schiaparelli_hem, "Title": "Cerebus", "image_url": cerebus_hem}]

    hemisphere_list

