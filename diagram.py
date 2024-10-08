from math import floor

BLACK = "\033[40m"
BLUE = "\033[44m"
file = open("sequence.txt")
s1, s2 = 0, 0


if __name__ == "__main__":
    for i in range(125):
        s1 += abs(float(file.readline()))
    for i in range(125):
        s2 += abs(float(file.readline()))
    
    s = s1 + s2
    per1, per2 = round(s1/s*100), round(s2/s*100)
    s1 = floor(round(s1/s*100)/5)
    s2 = floor(round(s2/s*100)/5)
    for i in range(max(s1, s2)):
        if s1 > s2:
            print(BLUE + " "*5 + BLACK + " "*10)
            s1 -= 1
        elif s1 == s2:
            print(BLUE + " "*5 + BLACK + " "*5 + BLUE + " "*5 + BLACK)
            s1 -= 1
            s2 -= 1
        else:
            print(BLACK + " "*10 + BLUE + " "*5 + BLACK)
            s2 -= 1
        print(f"s1({per1}%)" + "  " + f"s2({per2}%)")
