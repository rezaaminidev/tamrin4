numbers = []
count = 1
while count<=10:
    try:
        number = int(input("please write number ({}) :".format(count)))
        print(number)
        numbers.append(number)
        count+=1
    except:
        print("please write number corectly : ")
    1
minValue = numbers[0]
maxVaalue = numbers[0]
for i in numbers:
    if(i<minValue):
        minValue = i
    if(i>maxVaalue):
        maxVaalue = i

print("min Value : ", minValue)
print("max Value : ", maxVaalue)