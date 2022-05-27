import tkinter as tk
import random
import time

window = tk.Tk()
window.title('Blackjack')
window.configure(bg='green')

intro = tk.Label(text='Welcome to Blackjack. Good luck!', bg='green')
intro.grid(row=0, column=2, columnspan=3, padx=5, pady=5)
card_d1 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_d1.grid(row=1, column=1, padx=10, pady=5)
card_d2 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_d2.grid(row=1, column=2, padx=5, pady=5)
card_d3 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_d3.grid(row=1, column=3, padx=5, pady=5)
card_d4 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_d4.grid(row=1, column=4, padx=5, pady=5)
card_d5 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_d5.grid(row=1, column=5, padx=5, pady=5)
card_p1 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_p1.grid(row=4, column=1, padx=5, pady=5)
card_p2 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_p2.grid(row=4, column=2, padx=5, pady=5)
card_p3 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_p3.grid(row=4, column=3, padx=5, pady=5)
card_p4 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_p4.grid(row=4, column=4, padx=5, pady=5)
card_p5 = tk.Label(width=3, height=3, bg='green', font=('Verdana bold', '36'))
card_p5.grid(row=4, column=5, padx=5, pady=5)
score_d = tk.Label(bg='green')
score_d.grid(row=1, column=6, padx=5, pady=5)
score_p = tk.Label(bg='green')
score_p.grid(row=4, column=6, padx=5, pady=5)
message = tk.Label(bg='green')
message.grid(row=2, column=2, columnspan=3, padx=5, pady=5)
win_lose = tk.Label(bg='green', font=('Verdana bold', '36'))
win_lose.grid(row=3, column=2, columnspan=3, padx=5, pady=5)
cardsd = [card_d1, card_d2, card_d3, card_d4, card_d5]
cardsp = [card_p1, card_p2, card_p3, card_p4, card_p5]


class Cards:
    def __init__(self, suit, rank, card_value):
        """Used to create an object for each card"""
        self.suit = suit
        self.rank = rank
        self.card_value = card_value

    def reveal_card(self):
        print(f' -{self.rank} of {self.suit}')


suits = ['♠', '♥', '♣', '♦']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = []  # Create a standard 52 card deck
for suit in suits:
    for rank in ranks:
        deck.append(Cards(suit, rank, values[rank]))

player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0


def update_score(player_or_dealer):
    global player_score, dealer_score

    if player_or_dealer == 'player':
        player_score = 0
        for i in player_cards:
            player_score += values[i.rank]
            score_p['text'] = player_score
            if player_score > 21:  # Ace value from 11 to 1 if score > 21
                values['A'] = 1
                player_score = 0
                for j in player_cards:
                    player_score += values[j.rank]
                    score_p['text'] = player_score
                    if player_score > 21:
                        message['text'] = 'Bust!'
                        win_lose['text'] = 'You lose'

    elif player_or_dealer == 'dealer':
        dealer_score = 0
        for i in dealer_cards:
            dealer_score += values[i.rank]
            score_d['text'] = dealer_score
            if dealer_score > 21:  # Ace value from 11 to 1 if score > 21
                values['A'] = 1
                dealer_score = 0
                for j in dealer_cards:
                    dealer_score += values[j.rank]
                    score_d['text'] = dealer_score
                    if dealer_score > 21:
                        message['text'] = 'Dealer is bust!'
                        win_lose['text'] = 'You win'


def deal_card(player_or_dealer):
    global player_cards, dealer_cards, player_score, dealer_score
    dealt_card = random.choice(deck)
    if player_or_dealer == 'player':
        player_cards.append(dealt_card)
        update_score('player')
        cardsp[len(player_cards) - 1]['bg'] = 'white'
        if dealt_card.suit == '♥' or dealt_card.suit == '♦':
            cardsp[len(player_cards) - 1]['fg'] = 'red'
    elif player_or_dealer == 'dealer':
        dealer_cards.append(dealt_card)
        update_score('dealer')
        cardsd[len(dealer_cards) - 1]['bg'] = 'white'
        if dealt_card.suit == '♥' or dealt_card.suit == '♦':
            cardsd[len(dealer_cards) - 1]['fg'] = 'red'
    deck.remove(dealt_card)


def restart():
    global player_cards, dealer_cards
    message['text'] = ''
    win_lose['text'] = ''
    player_cards = []
    for i in range(len(cardsp)):
        cardsp[i]['text'] = ''
        cardsp[i]['bg'] = 'green'
        cardsp[i]['fg'] = 'black'
    dealer_cards = []
    for i in range(len(cardsd)):
        cardsd[i]['text'] = ''
        cardsd[i]['bg'] = 'green'
        cardsd[i]['fg'] = 'black'


def deal_cards():
    restart()
    for i in range(2):  # Deal 2 cards to player
        deal_card('player')
    card_p1['text'] = f'{player_cards[0].rank}   \n{player_cards[0].suit}\n   {player_cards[0].rank}'
    card_p1['bg'] = 'white'
    card_p2['text'] = f'{player_cards[1].rank}   \n{player_cards[1].suit}\n   {player_cards[1].rank}'
    card_p2['bg'] = 'white'
    for i in range(2):  # Deal 2 cards to dealer, one hidden
        deal_card('dealer')
    card_d1['text'] = f'{dealer_cards[0].rank}   \n{dealer_cards[0].suit}\n   {dealer_cards[0].rank}'
    card_d1['bg'] = 'white'
    card_d2['text'] = '?'
    card_d2['bg'] = 'white'
    card_d2['fg'] = 'grey'


def compare_score():
    if dealer_cards[1].suit == '♥' or dealer_cards[1].suit == '♦':
        cardsd[1]['fg'] = 'red'  # Colour dealer hidden card according to suit
    else:
        cardsd[1]['fg'] = 'black'
    if dealer_score > 21:
        message['text'] = 'Dealer went bust'
        win_lose['text'] = 'You win!'
    elif dealer_score < player_score <= 21:
        win_lose['text'] = 'You win!'
    elif player_score < dealer_score:
        win_lose['text'] = 'You lose'
    elif player_score == dealer_score:
        win_lose['text'] = 'Draw'


def hit_player():
    if player_score < 21 and win_lose['text'] == '':
        deal_card('player')
        cardsp[len(player_cards) - 1]['text'] = f'{player_cards[-1].rank}   \n{player_cards[-1].suit}' \
                                                f'\n   {player_cards[1].rank}'
        cardsp[len(player_cards) - 1]['bg'] = 'white'
    else:
        compare_score()


def hit_dealer():
    card_d2['text'] = f'{dealer_cards[1].rank}   \n{dealer_cards[1].suit}\n   {dealer_cards[1].rank}'
    if dealer_score < player_score and len(dealer_cards) < 5:
        while dealer_score < 17:
            deal_card('dealer')
            cardsd[len(dealer_cards) - 1]['text'] = f'{dealer_cards[-1].rank}   \n{dealer_cards[-1].suit}' \
                                                    f'\n   {dealer_cards[-1].rank}'
            cardsd[len(player_cards) - 1]['bg'] = 'white'
        compare_score()
    else:
        compare_score()


start_button = tk.Button(text='Deal Cards', width=7, command=deal_cards,
                         highlightbackground='green')  # bg not supported for buttons on Mac
start_button.grid(row=2, column=0, padx=5, pady=5)
hit_button = tk.Button(text='Hit', width=7, command=hit_player, highlightbackground='green')
hit_button.grid(row=2, column=6, padx=5, pady=5)
stand_button = tk.Button(text='Stand', width=7, command=hit_dealer, highlightbackground='green')
stand_button.grid(row=3, column=6, padx=5, pady=5)
window.mainloop()
