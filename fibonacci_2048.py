import random
import math

Board = list[list[int]]


def empty_board(n: int) -> Board:
    """Function that creates a board as a list of lists of ints, where all numbers are zero, in the form of an nxn matrix"""
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        result.append(row)
    return result


def random_position(n: int) -> tuple[int, int]:
    """Creates a tuple of random numbers between 0 and n"""
    return random.randint(0, n - 1), random.randint(0, n - 1)


def random_board(n: int) -> Board:
    """Creates an n-dimensional matrix board with two 1s in random positions"""
    result = empty_board(n)
    l = random_position(n)
    m = random_position(n)
    while l == m:
        l = random_position(n)
        m = random_position(n)
    result[l[0]][l[1]] = 1
    result[m[0]][m[1]] = 1
    return result


def fibo(n: int) -> int:
    """Function that indicates the index of the Fibonacci sequence for the number"""
    i = 0
    j = 1
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        while n != j:
            fibo_ant = j
            j = j + i
            i = fibo_ant
            result = result + 1
    return result


def transpose_matrix(t: Board) -> Board:
    """Function that transposes the board like a matrix"""
    transposed_board = []
    for i in range(len(t)):
        transposed_row = []
        for j in range(len(t)):
            transposed_row.append(t[j][i])
        transposed_board.append(transposed_row)
    return transposed_board


def slide_left(t: Board) -> Board:
    """To make a copy of a board, just like with a matrix, I transposed the board twice, since the transpose function
    would be used later for slide_up and slide_down functions. Thus, instead of creating a new function to copy boards,
    this one was recycled (and also because copying with [:] didn't work for the board). This generates another board
    equal to the initial one. Then, zeros are removed from the board, and using indices i and j, it iterates through all
    board positions comparing the left term with the right term. If two contiguous terms are consecutive Fibonacci terms,
    they are summed. A section had to be included in the if statement to ensure two 1s merge, since with the Fibonacci
    function used, 1 was only considered a single Fibonacci term. If two terms merge, they are summed and placed at the
    first term's position because it's a left slide, placing a zero in the second. Then j is incremented by 2 to compare
    the next two and avoid comparing zero with another number. Then zeros are removed again and appended at the end
    to have an nxn board again."""
    i = 0
    j = 0
    result = transpose_matrix(transpose_matrix(t))
    matrix_range = len(t[0])
    while i < len(t[0]):
        while result[i].count(0) > 0:
            result[i].remove(0)
        while j < len(result[i]) - 1:
            if fibo(result[i][j]) == (fibo(result[i][j + 1])) + 1 or fibo(result[i][j]) == (
            fibo(result[i][j + 1])) - 1 or (result[i][j] == 1 and result[i][j + 1] == 1):
                result[i][j] = result[i][j] + result[i][j + 1]
                result[i][j + 1] = 0
                j = j + 2
            else:
                j = j + 1
        while result[i].count(0) > 0:
            result[i].remove(0)
        while len(result[i]) < matrix_range:
            result[i].append(0)
        i = i + 1
        j = 0
    return result


def slide_right(t: Board) -> Board:
    """A function very similar to slide_left is used, except digits on the left now have priority,
    so indices j and i iterate from the end to the beginning, and j is decremented by 1 or 2 depending
    on whether two Fibonacci terms merged or not. Then instead of appending zeros at the end, they are
    inserted at the beginning, taking into account the initial board dimension."""
    i = 0
    result = transpose_matrix(transpose_matrix(t))
    matrix_range = len(t[0])
    while i < len(result[0]):
        while result[i].count(0) > 0:
            result[i].remove(0)
        j = len(result[i]) - 1
        while j > 0:
            if fibo(result[i][j]) == (fibo(result[i][j - 1])) + 1 or fibo(result[i][j]) == (
            fibo(result[i][j - 1])) - 1 or (result[i][j] == 1 and result[i][j - 1] == 1):
                result[i][j] = result[i][j] + result[i][j - 1]
                result[i][j - 1] = 0
                j = j - 2
            else:
                j = j - 1
        while result[i].count(0) > 0:
            result[i].remove(0)
        while len(result[i]) < matrix_range:
            result[i].insert(0, 0)
        i = i + 1
    return result


def slide_up(t: Board) -> Board:
    """To slide up, the board is transposed, then slid left, and then transposed back."""
    return transpose_matrix(slide_left(transpose_matrix(t)))


def slide_down(t: Board) -> Board:
    """To slide down, the board is transposed, then slid right, and then transposed back."""
    return transpose_matrix(slide_right(transpose_matrix(t)))


def board_changed_right(t: Board) -> int:
    """The board is copied with t[:] and then compared with the board slid to the right. If they are not equal,
    it returns 1, otherwise 0. Board_changed functions determine whether a move actually shifts terms on the board or not."""
    i = 0
    result = t[:]
    t = slide_right(t)
    if result != t:
        i = 1
    return i


def board_changed_down(t: Board) -> int:
    i = 0
    result = t[:]
    t = slide_down(t)
    if result != t:
        i = 1
    return i


def board_changed_left(t: Board) -> int:
    i = 0
    result = t[:]
    t = slide_left(t)
    if result != t:
        i = 1
    return i


def board_changed_up(t: Board) -> int:
    i = 0
    result = t[:]
    t = slide_up(t)
    if result != t:
        i = 1
    return i


def random_one_down(t: Board) -> Board:
    """This function uses the board_changed function and depending on whether the move is useful or not, creates a 1 at a
    random position on the board. An if and while were added to ensure the chosen position is a zero."""
    result = slide_down(t)
    n = len(t[0])
    if board_changed_down(t) == 1:
        k1 = random.randint(0, n - 1)
        k2 = random.randint(0, n - 1)
        while result[k1][k2] != 0:
            k1 = random.randint(0, n - 1)
            k2 = random.randint(0, n - 1)
        result[k1][k2] = 1
    return result


def random_one_up(t: Board) -> Board:
    result = slide_up(t)
    n = len(t[0])
    if board_changed_up(t) == 1:
        k1 = random.randint(0, n - 1)
        k2 = random.randint(0, n - 1)
        while result[k1][k2] != 0:
            k1 = random.randint(0, n - 1)
            k2 = random.randint(0, n - 1)
        result[k1][k2] = 1
    return result


def random_one_right(t: Board) -> Board:
    result = slide_right(t)
    n = len(t[0])
    if board_changed_right(t) == 1:
        k1 = random.randint(0, n - 1)
        k2 = random.randint(0, n - 1)
        while result[k1][k2] != 0:
            k1 = random.randint(0, n - 1)
            k2 = random.randint(0, n - 1)
        result[k1][k2] = 1
    return result


def random_one_left(t: Board) -> Board:
    result = slide_left(t)
    n = len(t[0])
    if board_changed_left(t) == 1:
        k1 = random.randint(0, n - 1)
        k2 = random.randint(0, n - 1)
        while result[k1][k2] != 0:
            k1 = random.randint(0, n - 1)
            k2 = random.randint(0, n - 1)
        result[k1][k2] = 1
    return result


def is_game_over(t: Board) -> bool:
    """This function tells you if the game ends at any point, which happens when all movements:
    left, right, down, and up are not useful movements."""
    i = True
    if board_changed_down(t) == 0 and board_changed_up(t) == 0 and board_changed_left(t) == 0 and board_changed_right(
            t) == 0:
        i = False
    return i


def check_win(t: Board) -> bool:
    """This function tells you if you have won. It iterates through all board terms and if any of them is 2584,
    it returns True, otherwise False."""
    victory = False
    i = 0
    j = 0
    while i < len(t[0]):
        while j < len(t[0]) and victory == False:
            if t[i][j] == 2584:
                victory = True
            else:
                j = j + 1
        i = i + 1
        j = 0
    return victory


def pretty_print_board(t: Board) -> int:
    """As the game progresses, numbers grow larger, and this function was included so that wouldn't modify
    the aesthetics and playability, ensuring each number is aligned with those above and below."""
    i = 0
    j = 0
    dim = len(t[0]) - 1
    k = 0
    spaces = ""
    while i < len(t[0]):
        if i != len(t[0]) - 1:
            while j < len(t[0]):
                while j != len(t[0]) - 1:
                    num = str(t[i][j])
                    digits = len(num)
                    while digits < 6:
                        k = k + 1
                        digits = digits + 1
                    while k > 0:
                        spaces = (spaces + " ")
                        k = k - 1
                    print(t[i][j], spaces, end="")
                    j = j + 1
                    k = 0
                    spaces = ""
                print(t[i][j])
                j = j + 1
        else:
            while j < len(t[0]) - 1:
                num = str(t[i][j])
                digits = len(num)
                while digits < 6:
                    k = k + 1
                    digits = digits + 1
                while k > 0:
                    spaces = (spaces + " ")
                    k = k - 1
                print(t[i][j], spaces, end="")
                j = j + 1
                k = 0
                spaces = ""
        i = i + 1
        j = 0
    return t[dim][dim]


def board_to_string(t: Board) -> str:
    """This function is used to save the game. It converts each number into a string and adds a comma,
    separating each different number on the board including zeros."""
    i = 0
    j = 0
    result = ""
    while i < len(t):
        while j < len(t):
            result = (result + str(t[i][j]) + ",")
            j = j + 1
        j = 0
        i = i + 1
    return result


def load_board_from_file() -> Board:
    """Reconverts the file with numbers and commas into a board."""
    with open("tablero.txt", "r") as f:
        j = 0
        i = 0
        matrix = []
        result = []
        mat = f.readline()
        length = mat.count(",")
        dim = math.sqrt(length)
        num = ""
        while j < len(mat):
            while i < int(dim):
                if mat[j] != ",":
                    num = num + mat[j]
                    j = j + 1
                else:
                    result.append(int(num))
                    num = ""
                    i = i + 1
                    j = j + 1
            matrix.append(result)
            result = []
            i = 0
        return matrix


def play_game(n: int) -> int:
    """The game function brings all functions together. First creates a random board and prints instructions,
    then loops through inputs to let the player play."""
    t = (random_board(n))
    print(pretty_print_board(t))
    result = True
    print("TO WIN, YOU NEED A NUMBER TO REACH 2584, GOOD LUCK. "
          "MOVEMENTS: r=right, l=left, d=down, u=up, end=quit game at any time, "
          "save=save game state, load=load saved game")
    i = 0
    while is_game_over(t) == True and result == True:
        print('What move would you like to make?')
        if check_win(t) == True and i == 0:
            print("You won!!! Do you want to keep playing?")
            play_again = input()
            if play_again == "si" or play_again == "yes":
                i = 1
                print('What move would you like to make?')
            elif play_again == "no":
                result = False
        if result == True:
            move = input()
            if move == 'r':
                t = random_one_right(t)
                print(pretty_print_board(t))
            elif move == 'd':
                t = random_one_down(t)
                print(pretty_print_board(t))
            elif move == 'u':
                t = random_one_up(t)
                print(pretty_print_board(t))
            elif move == 'l':
                t = random_one_left(t)
                print(pretty_print_board(t))
            elif move == 'end':
                result = False
            elif move == 'save':
                with open("tablero.txt", "w") as f:
                    f.write(board_to_string(t))
            elif move == 'load':
                t = load_board_from_file()
                print(pretty_print_board(load_board_from_file()))
            else:
                print("That is not a valid move")
    if is_game_over(t) == False:
        print("You lost, better luck next time.")
    return pretty_print_board(t)


def main():


    print("Starting full game:")
    play_game(4)


if __name__ == '__main__':
    main()
