import itertools
from tkinter import E

game = [[1, 1, 2],
        [2, 1, 2],
        [1, 2, 1]]


def win(current_game):

    # horizontal winner
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} is the winner horizontally!')
            return True

    # vertical winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f'Player {check[0]} is the winner vertically!')
            return True

    # diagonal winner
    diag = []

    for ix in range(len(game)):
        diag.append(game[ix][ix])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f'Player {diag[0]} is the winner diagonally \\!')
        return True

    diag = []

    for col, row in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f'Player {diag[0]} is the winner diagonally /!')
        return True
    
    return False


win(game)


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try: 
        if game[row][column] != 0:
            print("That position is occupied, choose another!")
            return game_map, False
        if just_display == False:
            game_map[row][column] = player
        print('   a  b  c')
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True 

    except Exception as e:
        print("Ops, something went wrong...", e)
        return game_map, False
    except Exception as e:
        print("Ops, something went wrong...", e)
        return game_map, False

    


play = True
player = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            col_choice = int(input("Choose column number (0, 1 ,2): "))
            row_choice = int(input("Choose row number (0, 1 ,2): "))
            game, played = game_board(game, current_player, row_choice, col_choice)

        if win(game):
            game_won = True
            again = input("Do you want to play again? (y/n): ")
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n":
                print("Byeeeeee")
                play = False 
            else:
                print("Not a valid answer sooo... see you later aligator.")
                play = False 