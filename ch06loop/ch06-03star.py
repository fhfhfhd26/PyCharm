# print("          \u2605")


for i in range(1, 10):
    if i < 6:
        for k in range(1, 6-i):
            print("  ", end="")
        for k in range(1, i*2):
            print("\u2605", end="")
    else:
        for k in range(1, i-4):
            print("　", end="")
        for k in range(1, (10-i)*2):
            print("\u2605", end="")
    print()

