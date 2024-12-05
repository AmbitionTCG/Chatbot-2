

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

    check_akronym = ["akronyms", "Akronyms", "akronym:", "Akronym:"]

    for i in check_akronym:
        if i in tokens:
            mening = " ".join((tokens))
            testar = mening.split(i)
            words = testar[1:]
            break

    akronym = ""
    for word in words[0].split(" "):
        if len(word) > 1:
            akronym += word[0]
            akronym += "."
    return akronym.upper()

