# write your code here
cells = list(input("Enter cells: "))


def create_board():
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def check_win(x_win, o_win):
    if x_win == 1 and o_win == 1:
        return "Both"
    if x_win == 1:
        return "X wins"
    if o_win == 1:
        return "O wins"


def check_vertical():
    x_win = 0
    o_win = 0
    for current_line in range(3):
        current_x = 0
        current_o = 0
        for i in range(0 + current_line, 7 + current_line, 3):
            if cells[i] == "X":
                current_x += 1
                if current_x == 3:
                    x_win = 1
            if cells[i] == "O":
                current_o += 1
                if current_o == 3:
                    o_win = 1
    return check_win(x_win, o_win)


def check_horizontal():
    x_win = 0
    o_win = 0
    for current_line in range(3):
        current_x = 0
        current_o = 0
        for i in range(current_line * 3, (current_line + 1) * 3):
            if cells[i] == "X":
                current_x += 1
                if current_x == 3:
                    x_win = 1
            if cells[i] == "O":
                current_o += 1
                if current_o == 3:
                    o_win = 1
    return check_win(x_win, o_win)


def check_diagonal():
    if "X" == cells[0] == cells[4] == cells[8] or "X" == cells[2] == cells[4] == cells[6]:
        return "X wins"
    if "Y" == cells[0] == cells[4] == cells[8] or "Y" == cells[2] == cells[4] == cells[6]:
        return "Y wins"


create_board()
if check_vertical() == "Both" or check_horizontal() == "Both" or abs(cells.count("X") - cells.count("O")) > 1:
    print("Impossible")
elif check_horizontal() is not None:
    print(check_horizontal())
elif check_vertical() is not None:
    print(check_vertical())
elif check_diagonal() is not None:
    print(check_diagonal())
elif "_" in cells:
    print("Game not finished")
else:
    print("Draw")
