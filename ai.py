import random
moves = list(range(0,10))
# print(moves)
def bot_move(turn, choice):
    if turn % 2 != 0:
        moves.remove(int(choice))
        bot_choice = random.choice(list(moves))
        return bot_choice
    else:
        pass
