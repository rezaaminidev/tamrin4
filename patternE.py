for i in range(7):
    for j in range(7):
        if((i == 0 or i==3 or i==6) and 0<=j<7):
            print(" * " ,end="")
        elif(0<i<7 and j==0):
            print(" * " , end="")

    print()    