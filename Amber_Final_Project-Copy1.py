#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 

def valid_input(player_input):
    return player_input in ["Rock", "Paper", "Scissors"]
def scorekeeper(player1_wins, player2_wins):
  return "Player 1: {}  Player 2: {}".format(player1_wins, player2_wins) 
def play_game():
    try:
        player_1_wins = 0
        player_2_wins = 0
        
        while True:
            if player_1_wins == 2:
                print("Player 1 wins the game!")
                break;
            elif player_2_wins == 2:
                print("Player 2 wins the game!")
                break;
            player_1 = input("Player 1, please choose Rock, Paper, or Scissors: ")
            player_2 = input("Player 2, please choose Rock, Paper, or Scissors: ")
            if not valid_input(player_1) or not valid_input(player_2):
                print("Invalid input. Please try again.")
                continue

            if player_1 == player_2:
                print("It's a tie!")
            elif player_1 == "Rock":
                if player_2 == "Paper":
                    print("Player 2 wins this round!")
                    player_2_wins += 1
                else: 
                    print("Player 1 wins this round!")
                    player_1_wins += 1
            elif player_1 == "Paper":
                if player_2 == "Scissors":
                    print("Player 2 wins this round!")
                    player_2_wins += 1
                else:
                    print("Player 1 wins this round!")
                    player_1_wins += 1
            elif player_1 == "Scissors":
                if player_2 == "Rock":
                    print("Player 2 wins this round!")
                    player_2_wins += 1
                else:
                    print("Player 1 wins this round")
    except:
        print("An error occurred. Please try again.")

while True:
  play_game()
print(player_1_wins, player_2_wins)




# In[ ]:




