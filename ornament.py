BLACK = "\033[40m"
WHITE = "\033[47m"


s1 = BLACK + " "*5 + WHITE + "  "
s2 = BLACK + " " + WHITE + " "*3 + BLACK + " " + WHITE + 2*" "
s3 = BLACK + " " + WHITE + " " + BLACK + " "*3 + WHITE + " "*2
s4 = BLACK + " " + WHITE + " " + BLACK + " "*1 + WHITE + " "*4
s5 = BLACK + " " + WHITE + " " + BLACK + " "*5

s = [s1, s2, s3, s4, s5]

if __name__ == "__main__":
    for i in s:
        for j in range(30):
            print(i, end="")
        print("")

