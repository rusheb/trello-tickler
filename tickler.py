from trello import TrelloClient
from datetime import datetime
import os
import json

with open('config.json') as f:
    config = json.load(f)

MY_BOARD = config['board_id']
TICKLER = config['tickler_id']
INBOX = config['inbox_id']

client = TrelloClient(
        api_key=config['trello_key'],
        api_secret=config['trello_secret']
        )

tickler = client.get_board(MY_BOARD).get_list(TICKLER)
today = datetime.now().date()

for card in tickler.list_cards():
    if card.due_date == '':
        print(f'does card {card} have a due date?')
        continue

    due = card.due_date.replace(tzinfo=None).date()
    if due <= today:
        card.remove_due()
        card.change_list(INBOX)
        card.set_pos('bottom')
