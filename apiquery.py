from newsapi import NewsApiClient


class APIQuery(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.client = NewsApiClient(api_key= self.api_key)
        

    def search(self, query, category):
        
        return self.client.get_top_headlines(q=query, category=category)['articles']

    

    



