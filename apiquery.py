"""
File Name: apiquery.py
Author: Akli Amrous
Copyright (c) Akli Amrous
Description: This is a simple wrapper for the 
News API allowing for a one call request

"""


from newsapi import NewsApiClient


class APIQuery(object):

    """
    Name: APIQuery
    Description: This is the class wrapper for the API
    The constructor accepts an api_key and creates a client
    object

    Class Methods:
    search(self, query, category):  -Query the API and return the results

    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = NewsApiClient(api_key= self.api_key)
        

    def search(self, query, category):
        # Make the call to the API with a specificed category and query
        # Return the dictionary of articles
        return self.client.get_top_headlines(q=query, category=category)['articles']

    

    



