import ui

RegVar = False

def RegFunc(write):
    print("regfunc here")
    RegVar = True
    with open('User_inputs.txt', 'w+') as f:
            f.write("\n" + write)
            print("file succesfully written in!")



