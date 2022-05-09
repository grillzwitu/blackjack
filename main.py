#!/usr/bin/python3
"""
  A game of blackjack
"""

import time
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

#the card deck
deck_of_cards = [2,3,4,5,6,7,8,9,"J","K","Q","A"] * 4

#shuffle the cards
random.shuffle(deck_of_cards)

#display the whole shuffled deck of cards
# for card in deck_of_cards:
#   print(card, end=' ')

#start the game
def game():
  player_cards =[]
  dealer_cards = []

#deal 2 cards to the player
  pick = 0
  while pick  < 2:
    player_pick = random.choice(deck_of_cards)
    player_pick_index = deck_of_cards.index(player_pick)
    player_cards.append(player_pick)

    #remove card from the deck of cards
    del deck_of_cards[player_pick_index]
    
    pick+=1

  #display the players cards
  time.sleep(1)
  print(f'\n\nYour card numbers are {", ".join([str(player_cards[0]), str(player_cards[1])])}', end= ' ')
  # for card in player_cards:
  #   print(f'{card}', end=' ')

  #deal cards for the dealer
  pick1 = 0
  while pick1  < 2:
    dealer_pick = random.choice(deck_of_cards)
    dealer_pick_index = deck_of_cards.index(dealer_pick)
    dealer_cards.append(dealer_pick)

    #remove card from the deck of cards
    del deck_of_cards[dealer_pick_index]

    pick1 += 1

  time.sleep(1)
  print(f'\nThe dealers first card number is {dealer_cards[0]}')

  #making decisions
  decisions = ["Hit", "Stand"]

  # get a decision from the player
  player_decision = input('\n🤔 Will you Hit or Stand, please type here: ').capitalize()

  #analyzing the player's decision
  while player_decision:
    if player_decision not in decisions:
      time.sleep(1)
      player_decision = input('\n🖐🏾 Enter either Hit or Stand: ').capitalize()
      continue
    else:
      if player_decision == decisions[0]:
        player_pick1 = random.choice(deck_of_cards)
        player_pick1_index = deck_of_cards.index(player_pick1)
        player_cards.append(player_pick1)

        #remove card from the deck of cards
        del deck_of_cards[player_pick1_index]
        break

      elif player_decision == decisions[1]:
        break

  #checking the player's cards, converting the alphabets to digits, and counting the sum
  for i in range(len(player_cards)):
    if player_cards[i] == "J" or player_cards[i] == "K" or player_cards[i] == "Q":
      player_cards[i] = 10
    if player_cards[i] == "A":
      player_cards[i] = 11


  #checking the dealer's card numbers, converting the alphabets to digits, and counting the sum to help the dealer make an informed decision
  for i in range(len(dealer_cards)):
    if dealer_cards[i] == "J" or dealer_cards[i] == "K" or dealer_cards[i] == "Q":
      dealer_cards[i] = 10
    if dealer_cards[i] == "A":
      dealer_cards[i] = 11

      if sum(dealer_cards) > 21:
        dealer_cards[i] = 1

  #print the card numbers
  time.sleep(1)
  print(f'\nThe dealer\'s card numbers are', end= ' ')
  for card in dealer_cards:
    time.sleep(0.5)
    print(f'{card}', end=' ')

  #taking the dealer's decision
  dealers_decision = ""

  #if the dealer's cards are less than 17 but greater than 13, the dealer randomly chooses to either hit or stand
  if sum(dealer_cards) < 17 and sum(dealer_cards) > 13 :
    dealers_decision = random.choice(decisions)

  #if the dealer's card numbers are greater than or equal 17 but less than or equal 21, the dealer chooses to stand
  elif sum(dealer_cards) >= 17 and sum(dealer_cards) <= 21 :
    dealers_decision = decisions[1]

  #if the dealer's card numbers are less than or equal 13, the dealer chooses to hit
  elif sum(dealer_cards) <= 13:
    dealers_decision = decisions[0]

  #if the dealer hits
  if dealers_decision == decisions[0]:
    time.sleep(1)
    print('\nThe dealer chose to hit')
    
    #deal another card for the dealer
    dealer_pick1 = random.choice(deck_of_cards)
    dealer_pick1_index = deck_of_cards.index(dealer_pick1)
    dealer_cards.append(dealer_pick1)

    #remove card from the deck of cards
    del deck_of_cards[dealer_pick1_index]

  #if the dealer chooses to stand
  elif dealers_decision == decisions[1]:
    print('\nThe dealer chose to stand')
    
  #checking the player's cards, converting the alphabets to digits, and counting the sum
  for i in range(len(player_cards)):
    if player_cards[i] == "J" or player_cards[i] == "K" or player_cards[i] == "Q":
      player_cards[i] = 10
    if player_cards[i] == "A":
      player_cards[i] = 11
      if sum(player_cards) > 21:
        player_cards[i] = 1

  #print the card numbers
  time.sleep(1)
  print(f'\nYour card numbers are', end= ' ')
  for card in player_cards:
    print(f'{card}', end=' ')

  #Print the sum of the card numbers
  time.sleep(1)
  print(f'\nThe sum of your cards is {sum(player_cards)}')

  #last check on the dealer's cards, converting the alphabets to digits, and counting the sum
  for i in range(len(dealer_cards)):
    if dealer_cards[i] == "J" or dealer_cards[i] == "K" or dealer_cards[i] == "Q":
      dealer_cards[i] = 10
    if dealer_cards[i] == "A":
      dealer_cards[i] = 11
      if sum(dealer_cards) > 21:
        dealer_cards[i] = 1

  #print the card numbers
  time.sleep(1)
  print(f'\nThe dealers card numbers are', end=' ')
  for card in dealer_cards:
    print(f'{card}', end=' ')

  #print sum of the card numbers
  time.sleep(1)
  print(f'\nThe sum of dealers cards is {sum(dealer_cards)}')

  #compare sum of card number f0r the palyer and the dealer and declare a winner
  if (sum(player_cards) > sum(dealer_cards) and sum(player_cards) <= 21) or (sum(player_cards) <= 21 and sum(dealer_cards) > 21):
    if sum(dealer_cards) > 21:
      time.sleep(1)
      print(f'\n The dealer is busted')

    time.sleep(1)
    print(f'\n🤩 🏆 You win you have {sum(player_cards)}, the dealer has {sum(dealer_cards)}')

  elif (sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) <= 21) or (sum(player_cards) > 21 and sum(dealer_cards) <= 21):
    if sum(player_cards) > 21:
      time.sleep(1)
      print(f'\n😢 The player is busted')

    time.sleep(1)
    print(f'\n😞 You lose you have {sum(player_cards)}, dealer has {sum(dealer_cards)}')

  elif (sum(player_cards) == sum(dealer_cards)) or (sum(player_cards) > 21 and sum(dealer_cards) > 21):
    if sum(player_cards) > 21 and sum(dealer_cards) > 21:
      time.sleep(1)
      print(f' Both the player and dealer are busted')
    
    time.sleep(1)
    print(f'\n🧨🧨 It\'s a tie you have {sum(player_cards)}, dealer has {sum(dealer_cards)}')

  # else:
    # print(f'\nWhat the hell just happened here 😯, you have {sum(player_cards)}, dealer has {sum(dealer_cards)}')

  user_input = input(f'Do you want to play again Y/N: ').upper()

  if user_input == "Y":
    game()
  else:
    return

game()