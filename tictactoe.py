Row1 = [' ', '|', ' ', '|', ' ']
Row2 = ['-', '+', '-', '+', '-']
Row3 = [' ', '|', ' ', '|', ' ']
Row4 = ['-', '+', '-', '+', '-']
Row5 = [' ', '|', ' ', '|', ' ']

def print_gameboard():
    print(''.join(Row1))
    print(''.join(Row2))
    print(''.join(Row3))
    print(''.join(Row4))
    print(''.join(Row5))

def welcome_message():
    print("TIC TAC TOE")
    print("Choose where to go.")
    print("123 on top, 456 in the middle, 789 on the bottom.")
    print("X goes first.")
    print_gameboard()

def user_input():
    userinput = int(input("Choose where to go "))
    return userinput

def update_gameboard(num):
    if num == 1 and len(availablelist) % 2 == 0:
        Row1[0] = 'X'
    elif num == 1 and len(availablelist) % 2 == 1:
        Row1[0] = 'O'
    elif num == 2 and len(availablelist) % 2 == 0:
        Row1[2] = 'X'
    elif num == 2 and len(availablelist) % 2 == 1:
        Row1[2] = 'O'
    elif num == 3 and len(availablelist) % 2 == 0:
        Row1[4] = 'X'
    elif num == 3 and len(availablelist) % 2 == 1:
        Row1[4] = 'O'
    elif num == 4 and len(availablelist) % 2 == 0:
        Row3[0] = 'X'
    elif num == 4 and len(availablelist) % 2 == 1:
        Row3[0] = 'O'
    elif num == 5 and len(availablelist) % 2 == 0:
        Row3[2] = 'X'
    elif num == 5 and len(availablelist) % 2 == 1:
        Row3[2] = 'O'
    elif num == 6 and len(availablelist) % 2 == 0:
        Row3[4] = 'X'
    elif num == 6 and len(availablelist) % 2 == 1:
        Row3[4] = 'O'
    elif num == 7 and len(availablelist) % 2 == 0:
        Row5[0] = 'X'
    elif num == 7 and len(availablelist) % 2 == 1:
        Row5[0] = 'O'
    elif num == 8 and len(availablelist) % 2 == 0:
        Row5[2] = 'X'
    elif num == 8 and len(availablelist) % 2 == 1:
        Row5[2] = 'O'
    elif num == 9 and len(availablelist) % 2 == 0:
        Row5[4] = 'X'
    elif num == 9 and len(availablelist) % 2 == 1:
        Row5[4] = 'O'

    print_gameboard()

def check_win():
    while 0 < len(availablelist) < 6:
        if Row1[0] == Row1[2] == Row1[4] == 'X':
            print("Player One Wins!")
            return True
        elif Row3[0] == Row3[2] == Row3[4] == 'X':
            print("Player One Wins!")
            return True
        elif Row5[0] == Row5[2] == Row5[4] == 'X':
            print("Player One Wins!")
            return True
        elif Row1[0] == Row3[0] == Row5[0] == 'X':
            print("Player One Wins!")
            return True
        elif Row1[2] == Row3[2] == Row5[2] == 'X':
            print("Player One Wins!")
            return True
        elif Row1[4] == Row3[4] == Row5[4] == 'X':
            print("Player One Wins!")
            return True
        elif Row1[0] == Row3[2] == Row5[4] == 'X':
            print("Player One Wins!")
            return True
        elif Row5[4] == Row3[2] == Row1[0] == 'X':
            print("Player One Wins!")
            return True
        elif Row1[0] == Row1[2] == Row1[4] == 'O':
            print("Player Two Wins!")
            return True
        elif Row3[0] == Row3[2] == Row3[4] == 'O':
            print("Player Two Wins!")
            return True
        elif Row5[0] == Row5[2] == Row5[4] == 'O':
            print("Player Two Wins!")
            return True
        elif Row1[0] == Row3[0] == Row5[0] == 'O':
            print("Player Two Wins!")
            return True
        elif Row1[2] == Row3[2] == Row5[2] == 'O':
            print("Player Two Wins!")
        elif Row1[4] == Row3[4] == Row5[4] == 'O':
            print("Player Two Wins!")
            return True
        elif Row1[0] == Row3[2] == Row5[4] == 'O':
            print("Player Two Wins!")
            return True
        elif Row5[4] == Row3[2] == Row1[0] == 'O':
            print("Player Two Wins!")
            return True
        else:
            validate_input(user_input())
    if len(availablelist) == 0:
        print("Draw! Want to play again?")
        welcome_message()
    else:
        pass

availablelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def validate_input(num):
    while 0 < num < 10:
        if num == 0:
            print("You can't go there!")
        elif num in availablelist:
            availablelist.remove(num)
            print(availablelist)
            update_gameboard(num)
            break
        else:
            print("You can't go there!")
            break


if __name__ == '__main__':

    welcome_message()
    validate_input(user_input())
    check_win()

    while check_win() != True and len(availablelist) > 0:
        validate_input(user_input())
        check_win()
    else:
        print("Game Over!")
