result = 1
counter = 0
while counter < 10:
    try:
        number = int(input("please write a number : "))
        result*=number
        counter+=1
    except :
        print("please write a number interger")

print("zarb adad shoma in mibashad ", result)


