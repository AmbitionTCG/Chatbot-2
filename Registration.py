import ui

RegVar = False


def RegFunc(write=""):

    global RegVar

    if write != "prova":
        with open('User_inputs.txt', 'a') as f:
            f.write('\n' + write)
            print("file succesfully written in!")
        RegVar = False
    else:
        RegVar = True

