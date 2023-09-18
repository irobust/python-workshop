import requests

response = requests.get('https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')

deck = response.json()

print(deck['deck_id'])

nextResponse = requests.get(f"https://www.deckofcardsapi.com/api/deck/{deck['deck_id']}/draw/?count=2")

cards = nextResponse.json()

for card in cards['cards']:
    print(card['image'])
# print(cards['cards'][0]['image'])
