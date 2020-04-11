from random import choice

suits = ['♣','♥', '♠', '♦']
ranks = [i for i in range (2,11)] + ['J', 'Q', 'K', 'A']
deck = [f'{suit} {rank}' for rank in ranks for suit in suits]

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.token = 100
        self.ready = False
    
    def count_points(self):
        cards_without_suits = []
        for card in self.cards:
            cards_without_suits.append(card.split()[-1])
        points = []
        for card in cards_without_suits:
            if card.isdigit():
                points.append(int(card))
            elif card == 'A':
                points.append(1)
            else: 
                points.append(0.5)
        self.points = sum(points)
        

def pick_card():
    card = choice(deck)
    deck.remove(card)
    return card


print("Press 'q' to finish.")
player_names = []
while True:
    player = input('Enter player names: ')
    if player == 'q':
        break
    else:
        player_names.append(player.title())

players = []
for player_name in player_names:
    players.append.(Player(player))

for player in players:
    bet = input(f'{player.name}, how much to bet?')
    player.bet = int(bet)

for player in players:
    player.cards.append(pick_card())
    player.count_points()
    print(f"{player.name}'s cards: {player.cards}. Points: {player.points}.")


while True:
    if all(player.ready for player in players):
        break
    
    for player in players:
        if not player.ready:
            if player.points < 10.5:
                response = input(f'{player.name}, pick 1 more card?')
                if response.lower() == 'y':
                    player.cards.append(pick_card())
                elif response.lower() == 'n':
                    player.ready = True
                player.count_points()
                if player.points >= 10.5:
                    player.ready = True
                    print(f'{player.name} lost. Points: {player.points}')

    for player in players:
        print(f"{player.name}'s cards: {player.cards}. Points: {player.points}.")

not_loser = [player for player in players if player.points <= 10.5]
winner = sorted(not_loser, key=lambda i:i.points)[-1]

for player in players:
    if player != winner:
        player.token -= player.bet
        winner.token += player.bet

print(f'{winner.name} won.')
print('Tokens:')
for player in players:
    print(f"{player.name}: {player.token}")
