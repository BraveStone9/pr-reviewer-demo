import requests


def fetch_remote_resource(url):
    return requests.get(url).text
