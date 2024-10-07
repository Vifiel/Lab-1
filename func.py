BLACK = "\033[40m"
WHITE = "\033[47m"


if __name__ == "__main__":
    for i in range(9):
        print(WHITE + " "*(12 - i - 3 - 1) + BLACK + " "*int(i<9) + WHITE + " "*(i+1) + BLACK)
    for i in range(3):
        print(WHITE + " "*10, end="")
        print("\033[0m")
