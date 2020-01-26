def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    ◯    ",
              "|   /|\    ",
              "|    |    ",
              "|   / \   ",
              "|         ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！英単語を当てよう！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "アルファベット１文字を入れてね！："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}。".format(word))

x = input("答えを入れてください：")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
hangman(x)
