import requests
import json

url = 'https://swapi.co/api/'


def get_api():
    r = requests.get(url)
    return r.json()


def get_people():
    uri = f'{url}people'
    r = requests.get(uri)
    return r.json()['results']


def find_people_by_name(name):
    uri = f'{url}people/?search={name}'
    r = requests.get(uri)
    return r.json()['results']


def get_films_character_was_in(name):
    pass