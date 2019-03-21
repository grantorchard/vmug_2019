import requests
import json
from prettytable import PrettyTable

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

def getdata(url):
    r = requests.get(url)
    if r.status_code == 200:
        print('success!')
        return r.json()
    else:
        print('Your father is disappointed in you')
        return r.status_code

def getcharacter(url, name):
    r = requests.get(url)
    for i in r.json()['results']:
        if i['name'] == name:
            return i
        else:
            print('Failure!')

