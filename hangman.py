def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|        |          ",
              "|        |          ",
              "|        0          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Dobro pozhalovat' na kazn'")
    print((" ".join(board)))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Vvedite bukvu: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("\nVi viigrali! Bilo zagadano slovo: {}.".format(word))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("\nVi proigrali! Bilo zagadano slovo: {}.".format(word))

import random
sluch_slovo = ["porebrik", "karton", "zhelezo", "samolet", "klaviatura",
               "sluchai", "pulemet", "kniha", "gitara", "vitaminy"]
hangman(random.choice(sluch_slovo))
