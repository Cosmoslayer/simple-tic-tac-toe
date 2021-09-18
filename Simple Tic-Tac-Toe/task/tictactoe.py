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
# if check_vertical() == "Both" or check_horizontal() == "Both" or abs(cells.count("X") - cells.count("O")) > 1:
#     print("Impossible")
# elif check_horizontal() is not None:
#     print(check_horizontal())
# elif check_vertical() is not None:
#     print(check_vertical())
# elif check_diagonal() is not None:
#     print(check_diagonal())
# elif "_" in cells:
#     print("Game not finished")
# else:
#     print("Draw")

while True:
    coordinates = input("Enter coordinates: ")
    column, row = tuple(list(coordinates.split(" ")))
    if not column.isnumeric() and not row.isnumeric():
        print("You should enter numbers!")
    elif int(column) > 3 or int(row) > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        coord_cells = [[cells[row + (column * 3)] for row in range(3)] for column in range(3)]
        print(coord_cells[int(column) - 1][int(row) - 1])
        print(column, row)
        if coord_cells[int(column) - 1][int(row) - 1] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            coord_cells[int(column) - 1][int(row) - 1] = "X"
            print("---------")
            print(f"| {coord_cells[0][0]} {coord_cells[0][1]} {coord_cells[0][2]} |")
            print(f"| {coord_cells[1][0]} {coord_cells[1][1]} {coord_cells[1][2]} |")
            print(f"| {coord_cells[2][0]} {coord_cells[2][1]} {coord_cells[2][2]} |")
            print("---------")
            break
