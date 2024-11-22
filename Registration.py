import ui

RegVar = False

def RegFunc():
    print("regfunc here")
    RegVar = True
    with open('User_inputs.txt', 'w+') as f:
            f.write('%s\n' %ui.user_input)
            print("file succesfully written in!")
    f.close()
