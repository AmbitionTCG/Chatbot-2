import ui

RegVar = False


def RegFunc(write="", issuecat=""):

    global RegVar

    if issuecat != "registrera för prova på dag":
        with open('User_inputs.txt', 'a') as f:
            f.write('\n' + write)
            print("file succesfully written in!")
        RegVar = False
    else:
        RegVar = True

