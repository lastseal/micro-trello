#! /usr/bin/env python3
# -*- coding: utf-8 -*

import trello
import json

board = trello.Board()

# data = board.find()
# print( json.dumps(data, sort_keys=True, indent=4) )

for x in board.getLists():
    print( str(x) )



# cards = trello.find('cards/open')
# print(cards)

# members = { x['id']: x['fullName'] for x in trello.find('members') }
# labels = { x['id']: x['name'] for x in trello.find('labels')}
# lists = { x['id']: x['name'] for x in trello.find('lists/open') }
