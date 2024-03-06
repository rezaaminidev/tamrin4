
def user_name (user):
    return user[::-1]

def main():
    userName = input("please enter your name : ")
    recive_user_name = user_name(userName)
    print("your name reversed is:" , recive_user_name)

main()