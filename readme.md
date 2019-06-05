# Craft Beer App Technical Report

## Introduction and Background

The formula for a perfect beer is non-existent. Throughout the world, beer has mass popularity with a range of taste options to meet consumer demand. However, some locations have a more abundant selection compared to others. While taste buds play a key role in like or dislike of a beer, there are some beers that rank a lot higher, and people can mutually agree on this. However, venue can make or break the experience of craft beers. Due to the increasing demand and growing market for beer "design", and the social construct of it, it would be useful to have an idea of top rated breweries in the United States. The purpose of this project is to develop a flask application that displays web scraped data from the top rated breweries from the untappd website.

## Methods and Data Source

The original data sources include the breweries.csv from Kaggle, and the web scrape from "untappd.com". The breweries chosen for the web scrape was a random sample of 20 breweries from the csv, which were identified through the search navigator on untappd.

## Cleaning and Transformation

The breweries csv required one column to be dropped. The name of the brewery, state, and city were retained. Additionally, "rating" was an empty column added before the scraping code was applied in order to populate the the column with the corresponding brewery's rating from untappd.

## Result Database

The scrape function stored the python dictionary in MongoDB, and bson.json was used to identify records from MongoDB. Flask templating was used to develop an HTML page that displays the data. The HTML page called craft.html provides a button that automatically performs the web scrape of the data. Web scraping of the untappd data was chosen due to the length of time needed to retrieve an API which did not meet the timeframe/turnaround requirements of the project. There were no CSVs available with rating information, but the brewery CSV from Kaggle provided a foundation of brewery names that could be pulled from the untappd in a random sample. Additionally, the CSV provided location info for future analysis and app development.

## Dashboard Example: 

![Dashboard](https://github.com/KristiBischoff/craftbeer/tree/master/Images/BrewApp_pic1.jpg)

