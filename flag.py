
print("\033[42m \n \n")
s = []
for i in range(8):
    if i <=7:
        s.append("\033[42m" + " "*((16-i)*6+(i)*3) + "\033[41m" + " "*(i+1)*6 + "\033[42m")
#Это точно круг, а не ромб!
for i in s:
    print(i)
for i in s[::-1]:
    print(i)
