# -*- coding: utf-8 -*

import requests
import logging
import os

API_KEY = os.getenv("TRELLO_API_KEY")
API_TOKEN = os.getenv("TRELLO_API_TOKEN")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")

##
#

class Card:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def getId(self):
        return self.data['id']

    def getName(self):
        return self.data['name']

    def getDesc(self):
        return self.data['desc']

    def getChecklist(self):

        url = "https://api.trello.com/1/checklists"
        data = []
        
        for idChecklist in self.data['idChecklists']:
                
            res = requests.get(f"{url}/{idChecklist}", params={
                "key": API_KEY,
                "token": API_TOKEN
            })
    
            if res.status_code != 200:
                raise Exception({"status": res.status_code, "message": res.text})
    
            data.append( res.json() )
    
        logging.debug("Checklist: %d", len(data))
        
        return data

    def getMembers(self):

        url = "https://api.trello.com/1/members"
        data = []
        
        for idMember in self.data['idMembers']:
                
            res = requests.get(f"{url}/{idMember}", params={
                "key": API_KEY,
                "token": API_TOKEN
            })
    
            if res.status_code != 200:
                raise Exception({"status": res.status_code, "message": res.text})
    
            data.append( res.json() )
    
        logging.debug("Members: %d", len(data))

        return data

    def getLabels(self):
        return [x['name'] for x in self.data['labels']]

    def getShortUrl(self):
        return self.data['shortUrl']
        
##
#

class List:

    def __init__(self, data):
        self.data = data
        self.url = f"https://api.trello.com/1/lists/{data['id']}"

    def __str__(self):
        return self.data

    def getId(self):
        return self.data['id']

    def getName(self):
        return self.data['name']

    def getCards(self):

        res = requests.get(f"{self.url}/cards", params={
            "key": API_KEY,
            "token": API_TOKEN
        })

        if res.status_code != 200:
            raise Exception({"status": res.status_code, "message": res.text})

        data = res.json()

        logging.debug("cards: %d", len(data))

        return [Card(x) for x in data]

##
#

class Board:

    def __init__(self, id = BOARD_ID):
        self.url = f"https://api.trello.com/1/boards/{id}"

    def find(self):

        res = requests.get(f"{self.url}", params={
            "key": API_KEY,
            "token": API_TOKEN
        })

        if res.status_code != 200:
            raise Exception({"status": res.status_code, "message": res.text})

        data = res.json()

        logging.debug("data: %d", len(data))

        return data
    
    def getLists(self):

        res = requests.get(f"{self.url}/lists", params={
            "key": API_KEY,
            "token": API_TOKEN
        })

        if res.status_code != 200:
            raise Exception({"status": res.status_code, "message": res.text})

        data = res.json()

        logging.debug("lists: %d", len(data))

        return [List(x) for x in data]

##
#

def get(uri):

    res = requests.get(f"https://api.trello.com/1/{uri}", params={
        "key": API_KEY,
        "token": API_TOKEN
    })

    if res.status_code != 200:
        raise Exception({"status": res.status_code, "message": res.text})

    data = res.json()

    logging.debug("data: %s", data)

    return data
