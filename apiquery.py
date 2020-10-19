"""
File Name: apiquery.py
Author: Akli Amrous
Copyright (c) Akli Amrous 2020
Description: This is a simple wrapper for the 
News API allowing for a one call request

"""
from newsapi import NewsApiClient
from datetime import datetime as dt

class APIQuery(object):

    """
    Name: APIQuery
    Description: This is the class wrapper for the API
    The constructor accepts an api_key and creates a client
    object

    Class Methods:
    search(self, query, category):  -Query the API and return the results
    parse(self, results):           -Parse the data
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = NewsApiClient(api_key= self.api_key)
        

    def search(self, query, category):
        # Make the call to the API with a specificed category and query
        # Return the dictionary of articles
        print(category)
        return self.client.get_top_headlines(q=query, category=category)

    
    def parse(self, results):
        # This is a function to parse the data
        # Into a displayable format
        sources = []
        headlines = []
        date_published = []
        cover_images = []
        links = []
        descriptions = []
        for article in results['articles']:
            sources.append(article['source']['name'])
            headlines.append(article['title'])
            date_published.append(article['publishedAt'].split("T")[0])
            cover_images.append(article['urlToImage'])
            links.append(article['url'])
            descriptions.append(article['description'])

        parsed = {

            'sources': sources,
            'headlines': headlines,
            'date_published': date_published,
            'cover_images': cover_images,
            'links': links,
            'descriptions': descriptions

        }

        return parsed

        
        

    



