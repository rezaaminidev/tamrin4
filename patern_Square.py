for row in range(5):
    for col in range(5):
        if (0 < row < 4) and (0 < col < 4):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

