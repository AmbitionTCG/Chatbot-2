import ui

RegVar = False
currentUserInput = ""

def RegFunc():
    print("regfunc here")
    RegVar = True
    currentUserInput = ui.user_input
    if ui.user_input != currentUserInput:
        print("Edit into excel code here")