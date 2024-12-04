

def rövarspråk(tokens: list) -> str:
    konsonanter = "bcdfghjklmnpqrstvwxz"
    output = ""

    check_rövarspråk = ["Rövarspråk", "rövarspråk", "Rövarspråk:", "rövarspråk:"]

    for i in tokens:
        if i in check_rövarspråk:
            index = tokens.index(i)
            break
    

    for i in range(index+1):
        del tokens[i]
    

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
            break
    

    for i in range(index+1):
        del tokens[i]


    words = tokens
    akronym = ""
    for word in words:
        akronym += word[0]
        akronym += "."
    return akronym.upper()

