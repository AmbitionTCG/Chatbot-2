

def rövarspråk(tokens: list) -> str:
    konsonanter = "bcdfghjklmnpqrstvwxz"
    output = ""

    check_rövarspråk = ["Rövarspråk", "rövarspråk", "Rövarspråk:", "rövarspråk:"]

    for i in tokens:
        if i in check_rövarspråk:
            index = tokens.index(i)
            break
    
    print("rövaraspråk: " + str(tokens))
    for i in range(index + 1):
        del tokens[0]
    print("rövaraspråk: " + str(tokens))
    

    for letter in str(tokens):
        output += letter
        if letter.lower() in konsonanter:
            output += "o" + letter.lower()
    return output

def medelvärde(*tal: int) -> float:
    medelvärde = sum(tal)/len(tal)
    return medelvärde

def akronym(tokens: str) -> str:

    check_akronym = ["akronym", "Akronym", "akronym:", "Akronym:"]

    for i in tokens:
        if i in check_akronym:
            index = tokens.index(i)
            print(index)
            break
    

    print("Akronym: " + str(tokens) + str(index))
    for i in range(index + 1):
        print(i)
        del tokens[0]
    print("Akronym: " + str(tokens))


    
    akronym = ""
    for word in tokens:
        akronym += word[0]
        akronym += "."
    return akronym.upper()

