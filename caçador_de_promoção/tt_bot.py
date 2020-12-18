import twitter as tp
import json
from time import sleep
import random

API_KEY = 'lxUHEHc4UILwZZHfGe5OwPz9q'
API_SECRET_KEY = 'nioUiwuPcGFwFMrc4BhO9WzBsDDOrzeh9i4499tDfphaRnMznt'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJ%2FiKgEAAAAAZC3rRqPvLcW6pG87Hy8sPd%2BrceM%3DgNVNh5XOkrHZCkKY3yHLnDeon7QfNSaENgeGjQmsayJqoCtC7u'
ACCESS_TOKEN = '1339337234005286918-BtFxGbo4AgqhNUTfEVqWtXafxhQdv4'
ACCESS_TOKEN_SECRET = 'JaElajEbvgQjytRQPFje0gl4TiggNq5KI8xE6nXe8qMsX'


def get_Api():
    return tp.Api(consumer_key=API_KEY,
                  consumer_secret=API_SECRET_KEY,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


api = get_Api()


def product_list_maker():  # função que transforma de arquivo json para ziplist
    list_names = []
    list_links = []
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        for line in data:
            list_names += [line['name']]
            list_links += [line['link']]
        names_prices_links = list(zip(list_names, list_links))
    return names_prices_links


def thread_maker(thread_header):
    product_list_maker()
    original_tweet = api.PostUpdate(thread_header)
    for column in product_list_maker():
        message = f'{column[0]}\n{column[1]}'
        next_message = api.PostUpdate(message, in_reply_to_status_id=original_tweet.id, auto_populate_reply_metadata=True)
        number = random.uniform(1, 4)
        number = float('{:.2f}'.format(number))
        sleep(number)
        original_tweet = next_message
        print('------PRODUTO POSTADO------')
    print('------THREAD FEITA------')
