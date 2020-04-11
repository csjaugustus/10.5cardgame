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
        self.bet = 0 
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

players = {}
for player in player_names:
    players[player] = Player(player)

for player in players:
    bet = input(f'{player}, how much to bet?')
    players[player].bet = int(bet)

for player in players:
    players[player].cards.append(pick_card())
    players[player].count_points()
    print(f"{player}'s cards: {players[player].cards}. Points: {players[player].points}.")


while True:
    if all(players[player].ready for player in players):
        break
    
    for player in players:
        if not players[player].ready:
            if players[player].points < 10.5:
                response = input(f'{player}, pick 1 more card?')
                if response.lower() == 'y':
                    players[player].cards.append(pick_card())
                elif response.lower() == 'n':
                    players[player].ready = True
                players[player].count_points()
                if players[player].points >= 10.5:
                    players[player].ready = True
                    print(f'{player} lost. Points: {players[player].points}')

    for player in players:
        print(f"{player}'s cards: {players[player].cards}. Points: {players[player].points}.")

not_loser = [players[player] for player in players if players[player].points <= 10.5]
winner = sorted(not_loser, key=lambda i:i.points)[-1]

for player in players:
    if player != winner.name:
        players[player].token -= players[player].bet
        players[winner.name].token += players[player].bet

print(f'{winner.name} won.')
print('Tokens:')
for player in players:
    print(f"{player}: {players[player].token}")
