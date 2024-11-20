import ui


RegVar = False
currentuserinput = ""

def RegFunc():
    print("regfunc here")
    RegVar = True
    currentuserinput = ui.user_input
    if currentuserinput != ui.user_input:
        print(ui.user_input)
