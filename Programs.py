

def rövarspråk(user_input: str) -> str:
    konsonanter = "bcdfghjklmnpqrstvwxz"
    output = ""
    for letter in user_input:
        output += letter
        if letter.lower() in konsonanter:
            output += "o" + letter.lower()
    return output

def medelvärde(*tal: int) -> float:
    medelvärde = sum(tal)/len(tal)
    return medelvärde

def akronym(user_input: str) -> str:
    words = user_input.split()
    akronym = ""
    for word in words:
        akronym += word[0]
        akronym += "."
    return akronym.upper()

