import ui

RegVar = False
currentuserinput = ""

def RegFunc():
    print("regfunc here")
    RegVar = True
    currentuserinput = ui.user_input
    if currentuserinput != ui.user_input:
        with open('User_inputs.txt', 'w+') as f:
            f.write('%s\n' %ui.user_input)
            print("file succesfully written in!")
            f.close()
