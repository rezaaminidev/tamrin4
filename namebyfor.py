def user_name(name):
    reverce_name = ""
    for i in name:
        reverce_name = i + reverce_name
        
    return reverce_name
def main():
    user_names = input("please write your name : ")
    reversed_user_name = user_name(user_names)
    print("Your name reverced is : " , reversed_user_name)
main()