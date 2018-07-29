### Amy Vo 29305960 Project 3 Lab 2 ###

#This module contains functions that will deal with the
#MapQuest API and create search urls. 

import json
import urllib.parse
import urllib.request

API_KEY = urllib.parse.unquote('Fmjtd%7Cluu821u8nh%2Cbn%3Do5-94bnuw', encoding = 'utf-8')
BASE_URL = 'http://open.mapquestapi.com/directions/v2/route?'


def build_search_url(addresses_list) -> str:
    '''Create and return search URL with user input of addresses'''
    query_parameters = [
        ('key', API_KEY),
        ('from', addresses_list[0]),
    ]
    
    for address in addresses_list[1:]:
        query_parameters.append(('to', address))
    search_url = BASE_URL + urllib.parse.urlencode(query_parameters)
    return search_url

def get_result(search_url: str) -> 'json':
    '''Take in search url and return Python object representing the
    parsed JSON response'''
    response = None
    
    try:
        response = urllib.request.urlopen(search_url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()
