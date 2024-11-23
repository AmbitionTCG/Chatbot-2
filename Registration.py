import ui

RegVar = False

def RegFunc(write="erm, what the sigma"):
    print("regfunc here")
    RegVar = True
    with open('User_inputs.txt', 'w+') as f:
            f.write(write)
            print("file succesfully written in!")


