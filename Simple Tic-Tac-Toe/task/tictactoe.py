# write your code here
cells = [[" " for _ in range(3)] for _ in range(3)]
pattern = ["X", "O"]
counter = 0


def create_board():
    print("---------")
    print(f"| {cells[0][0]} {cells[0][1]} {cells[0][2]} |")
    print(f"| {cells[1][0]} {cells[1][1]} {cells[1][2]} |")
    print(f"| {cells[2][0]} {cells[2][1]} {cells[2][2]} |")
    print("---------")


def check_win(x_win=False, o_win=False):
    if x_win:
        return "X wins"
    if o_win:
        return "O wins"


def check_straight(value=""):
    x_win = False
    o_win = False
    for rows in range(3):
        current_cells = []
        for columns in range(3):
            if value == "vertical":
                current_cells.append(cells[columns][rows])
            if value == "horizontal":
                current_cells.append(cells[rows][columns])
        if all([x == "X" for x in current_cells if len(current_cells) == 3]):
            x_win = True
        elif all([x == "O" for x in current_cells if len(current_cells) == 3]):
            o_win = True
    return check_win(x_win, o_win)


def check_diagonal():
    if "X" == cells[0][0] == cells[1][1] == cells[2][2] or "X" == cells[0][2] == cells[1][1] == cells[2][0]:
        return "X wins"
    if "O" == cells[0][0] == cells[1][1] == cells[2][2] or "O" == cells[0][2] == cells[1][1] == cells[2][0]:
        return "O wins"


create_board()
while True:
    coordinates = input("Enter coordinates: ")
    column, row = tuple(list(coordinates.split(" ")))
    if not column.isnumeric() and not row.isnumeric():
        print("You should enter numbers!")
    elif int(column) > 3 or int(row) > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        if cells[int(column) - 1][int(row) - 1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            cells[int(column) - 1][int(row) - 1] = pattern[counter % 2]
            create_board()
            if check_straight("horizontal") is not None:
                print(check_straight())
                break
            elif check_straight("vertical") is not None:
                print(check_straight())
                break
            elif check_diagonal() is not None:
                print(check_diagonal())
                break
            elif not any(" " in sublist for sublist in cells):
                print("Draw")
                break
            counter += 1
