from helper import draw_board, check_turn, check_for_win
import os
from math import inf
#from ai import bot_move

spots = {
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : '10'
}

playing = True
complete = False
turn = 0
prev_turn = -1
Simple_Human = "O"
AI_Master = "X"
#change it so X or O can go first

scores = {
    "X" : 1,
    "O" : -1,
    "tie" : 0
}
# def minimax(board_object, ai):
#     if playing == False and complete == True and check_for_win(spots):
#         return scores[check_turn(prev_turn)]
#     elif turn > 8:
#         return scores["tie"]

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(draw_board(spots))
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    # if turn % 2 == 0:
    #     print("Human Player" + str(check_turn(turn)) + " turn: Pick your spot or press q to quit")
    #     choice = input()
    # else:
    #     print("Bot Player" + str(check_turn(turn)) + " turn: Pick your spot or press q to quit")
    #     choice = str(bot_move(turn, choice))
    #print("Player " + str(check_turn(turn)) + "'s turn: Pick your spot or press q to quit")
    choice = input()
    if choice == 'q':
        playing = False

    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {AI_Master, Simple_Human}:
            spots[int(choice)] = check_turn(turn)
            turn += 1

    #print(minimax(draw_board, AI_Master))
        # else:
        #     raise Exception("Spot is already occupied")
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False

os.system('cls' if os.name == 'nt' else 'clear')
print(draw_board(spots))

if complete:
    if check_turn(prev_turn) == AI_Master:
        print("Player AI Wins!")
    else:
        print("Player Human Wins!")
else:
    print("Tie")

print("Thanks for playing!")
