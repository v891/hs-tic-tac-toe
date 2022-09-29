# write your code here
# game_Input = input()


def print_field(input_li):
    print("---------")
    print("|", input_li[0], input_li[1], input_li[2], "|")
    print("|", input_li[3], input_li[4], input_li[5], "|")
    print("|", input_li[6], input_li[7], input_li[8], "|")
    print("---------")


def get_list(input_str):
    return list(input_str)


def is_impossible(input_li):
    sum_x = sum([1 for x in input_li if x == 'X'])
    sum_o = sum([1 for x in input_li if x == 'O'])
    if abs(sum_x - sum_o) > 1:
        return True


def x_win_times(input_li):
    count = 0
    rows = [1 for x in range(0, 9, 3) if input_li[x] + input_li[x + 1] + input_li[x + 2] == 'XXX']
    cols = [1 for x in range(3) if input_li[x] + input_li[x + 3] + input_li[x + 6] == 'XXX']
    if input_li[0] == "X" and input_li[4] == "X" and input_li[8] == "X":
        count += 1
    elif input_li[2] == "X" and input_li[4] == "X" and input_li[6] == "X":
        count += 1
    return count + sum(rows) + sum(cols)


def o_win_times(input_li):
    count = 0
    rows = [1 for x in range(0, 9, 3) if input_li[x] + input_li[x + 1] + input_li[x + 2] == 'OOO']
    cols = [1 for x in range(3) if input_li[x] + input_li[x + 3] + input_li[x + 6] == 'OOO']
    if input_li[0] == "O" and input_li[4] == "O" and input_li[8] == "O":
        count += 1
    elif input_li[2] == "O" and input_li[4] == "O" and input_li[6] == "O":
        count += 1
    return count + sum(rows) + sum(cols)


def are_two_wins(input_li):
    x_times = x_win_times(input_li)
    o_times = o_win_times(input_li)
    return x_times > 1 or o_times > 1 or x_times + o_times > 1


def is_draw(input_li):
    print(sum([1 for x in input_li if x == " "]))
    return sum([1 for x in input_li if x == " "]) == 0


def get_current_val(input_li, x, y):
    three_three = [input_li[v:v + 3] for v in range(0, 9, 3)]
    return three_three[x - 1][y - 1]


def update_current_val(input_li, x, y, v):
    k = 0
    if x == 1:
        k = -1
    elif x == 2:
        k = 2
    else:
        k = 5
    input_li[k + y] = v
    return input_li


def move(input_li, v):
    try:
        x, y = [int(x) for x in input().split()]
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            return move(input_li, v)
        cur = get_current_val(input_li, x, y)
        if cur == 'X' or cur == 'O':
            print("This cell is occupied! Choose another one!")
            return move(input_li, v)
        return update_current_val(input_li, x, y, v)
    except ValueError:
        print("You should enter numbers!")
        return move(input_li, v)


input_list = get_list([" " for x in range(9)])
print_field(input_list)

while not x_win_times(input_list) or not o_win_times(input_list) or not is_draw(input_list):
    move(input_list, "X")
    print_field(input_list)
    if x_win_times(input_list):
        print("X wins")
        break
    elif is_draw(input_list):
        print("Draw")
        break

    move(input_list, "O")
    print_field(input_list)
    if o_win_times(input_list):
        print("O wins")
        break
    elif is_draw(input_list):
        print("Draw")
        break


# if is_impossible(input_list):
#     print("Impossible")
# elif are_two_wins(input_list):
#     print("Impossible")
# elif x_win_times(input_list):
#     print("X wins")
# elif o_win_times(input_list):
#     print("O wins")
# elif is_draw(input_list):
#     print("Draw")
# else:
#     # print_field(move_x(input_list))
