

def rövarspråk(tokens: list[str]) -> str:
    konsonanter = "bcdfghjklmnpqrstvwxz"
    output = ""
    tokens_str = ""
    
    check_rövarspråk = ["Rövarspråk", "rövarspråk", "Rövarspråk:", "rövarspråk:"]

    for i in tokens:
        if i in check_rövarspråk:
            index = tokens.index(i)
            break
    
    for i in range(index + 1):
        del tokens[0]
    
    for i in tokens:
        tokens_str += i
        tokens_str += " "

    for letter in tokens_str:
        output += letter
        if letter.lower() in konsonanter:
            output += "o" + letter.lower()
    return output



def medelvärde(tokens: list[str]) -> str:
    tal = []
    for i in tokens:
        if i.isdigit() == True:
            tal.append(int(i))

    medelvärde = sum(tal)/len(tal)
    return "Medelvärdet är: " + str(medelvärde)

def akronym(tokens: list[str]) -> str:

    check_akronym = ["akronyms:", "Akronyms:", "akronym:", "Akronym:", "akronym", "Akronym", "akronyms", "Akronyms"]

    for i in tokens:
        if i in check_akronym:
            index = tokens.index(i)
            print(index)
            break
    

    for i in range(index + 1):
        print(i)
        del tokens[0]


    
    akronym = ""
    for word in tokens:
        akronym += word[0]
        akronym += "."
    return akronym.upper()

