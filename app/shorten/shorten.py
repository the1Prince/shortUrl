from flask import jsonify
import requests


def shortener(user_url):
    '''this is the function that consumes the shrtcode.de api to generate short url'''
    base_url='https://api.shrtco.de/v2/shorten?url='
     

    long_url=base_url + user_url
    print=long_url

    payload={}
    headers = {}
    #####although their documentation indicates its possible to use a POST request, I find the GET request more friendly
    response = requests.request("GET", long_url, headers=headers, data=payload)

    return jsonify(response.text)