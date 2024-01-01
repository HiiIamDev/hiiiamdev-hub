import os

def feature():
    print ("No Function in here, work in proggres... get out you mtfkers!")
    print ("0. Quit")

    print('\n')
    menu()

def menu():
    print ("**Select Function With numbers**\n")
    while True:
        user_desc = input("$ ")
        #print (user_desc)
        #print (type(user_desc))
        if (user_desc.isdigit() != True):
            print("You Cocksucker! How tf you can't reading about **Select Function With numbers**?!")
        else:
            x = int(user_desc)
            if (x == 0):
                os.system('cls')
                print('Goodbye my nigga!')
                break
            else: 
                print(f'READ THE FUCKING FUNCTION YOU FUCKING LIL NIGGA! WTF IS {x}?')

def opening():
    os.system('cls')
    print('Hello My Niggers!')
    print('Wellcome to')
    print("                                                                 ")
    print("██░ ██  ██▓ ██▓ ██▓ ▄▄▄       ███▄ ▄███▓▓█████▄ ▓█████ ██▒   █▓  ")
    print("▓██░ ██▒▓██▒▓██▒▓██▒▒████▄    ▓██▒▀█▀ ██▒▒██▀ ██▌▓█   ▀▓██░   █▒ ")
    print("▒██▀▀██░▒██▒▒██▒▒██▒▒██  ▀█▄  ▓██    ▓██░░██   █▌▒███   ▓██  █▒░ ")
    print("░▓█ ░██ ░██░░██░░██░░██▄▄▄▄██ ▒██    ▒██ ░▓█▄   ▌▒▓█  ▄  ▒██ █░░ ")
    print("░▓█▒░██▓░██░░██░░██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▓ ░▒████▒  ▒▀█░   ")
    print("▒ ░░▒░▒░▓  ░▓  ░▓   ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░    ")
    print("▒ ░▒░ ░ ▒ ░ ▒ ░ ▒ ░  ▒   ▒▒ ░░  ░      ░ ░ ▒  ▒  ░ ░  ░  ░ ░░    ")
    print("░  ░░ ░ ▒ ░ ▒ ░ ▒ ░  ░   ▒   ░      ░    ░ ░  ░    ░       ░░    ")
    print("░  ░  ░ ░   ░   ░        ░  ░       ░      ░       ░  ░     ░    ")
    print("                                        ░                 ░     HUB! ")
    print("Follow Me!")
    print("Github: @HiiIamDev")
    print('Instagram: @rtm.nyata \n\n')
    feature()


opening()