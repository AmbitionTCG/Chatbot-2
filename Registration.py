import ui
from ui import user_input

RegVar = False
currentuserinput = ""

def RegFunc():
    print("regfunc here")
    RegVar = True
    currentuserinput = ui.user_input
    if currentuserinput != user_input:
        print(user_input)
