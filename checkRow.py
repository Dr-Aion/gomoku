row = [".", ".", ".", ".", ".", ".", ".", "o", "o", "o", "o", "o", ".", ".", "."]
cur_player = "o"
count = 0
flag = False
for slot in row:
    if slot == cur_player and count == 0:
        count = count + 1
        flag = True
    elif slot == cur_player and flag:
        count = count + 1
        if count == 5:
            print("You won")
    else:
        count = 0
        flag = False
print(count)