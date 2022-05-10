import json 
import os 
import requests 


class ApiConnector:
    '''
    1. iterate through json content.
    2. get the data.
    3. push the data to posgres db.
    '''

    def __init__(self, api_base_url, directory):
        self.api_base_url = api_base_url
        self.headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.directory = 
