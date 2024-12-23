import languageModel

def hitta_enheter(tokens: list[str]) -> list[str]:
    
    enheter = [
    "Centimeter", "centimeter", "cm", "Meter", "meter", "m", "kilometer", "Kilometer", "km", "Millimeter", "millimeter", "mm",
    "Tum", "tum", "in", "Fot", "fot", "ft", "Yard", "yard", "yd", "Mile", "mile", "mi",
    
    "Gram", "gram", "g", "Kilogram", "kilogram", "kg", "Ton", "ton", "t", "Milligram", "milligram", "mg",
    "Ounce", "ounce", "oz", "Pound", "pound", "lb", "Stone", "stone", "st",
    
    "Liter", "liter", "l", "Milliliter", "milliliter", "ml", "Kubikmeter", "kubikmeter", "m³",
    "Kubikcentimeter", "kubikcentimeter","cm³", "Gallon", "gallon", "gal",
    "Quart", "quart", "qt", "Pint", "pint", "pt", "Cup", "cup",
    
    "Celsius", "celsius", "C", "Fahrenheit", "fahrenhiet", "F", "Kelvin", "kelvin", "K", "Rankine", "rankine", "R"
]
    output = []
    for i in tokens:
        if i in enheter:
            output.append(i)
            if len(output) == 2:
                return output

def omvandlare(tokens: list[str], filteredtokens: list[str]) -> str:
    lista_att_refrerera = {
        0.000001: ["Kubikcentimeter", "kubikcentimeter", "cm³"],
        0.001: ["Milliliter", "milliliter", "ml", "Millimeter", "millimeter", "mm", "Milligram", "milligram", "mg"],
        0.01: ["Centimeter", "centimeter", "cm"],
        0.24: ["Cup", "cup"],
        0.568261: ["Pint", "pint", "pt"],
        1: ["Meter", "meter", "m", "liter", "Liter", "l", "Kubikmeter", "kubikmeter", "m³", "Gram", "gram", "g"],
        1.101220: ["Quart", "quart", "qt"],
        2.54: ["Tum", "tum", "in"],
        3.785: ["Gallon", "gallon", "gal"],
        30.48: ["Fot", "fot", "ft"],
        31.1: ["Ounce", "ounce", "oz"],
        91.44: ["Yard", "yard", "yd"],
        373.2: ["Pound", "pound", "lb"],
        1000: ["Kilogram", "kilogram", "kg", "Kilometer", "kilometer", "km"],
        6350.29318: ["Stone", "stone", "st"],
        160934.4: ["Mile", "mile", "mi"],
        1000000: ["Ton", "ton", "t"]
    }

    list_of_enhet = []

    for i in filteredtokens:
        for category, keywords in lista_att_refrerera.items():
            if i in keywords:
                list_of_enhet.append(category)
            


    if languageModel.find_int(tokens) == None:
        return "Ber om ursäkt men kunde inte hitta ett tal i din mening!"
    else:
        match filteredtokens[0]:
            case "Celsius" | "celsius" | "C":
                match filteredtokens[1]:
                    case "Fahrenheit" | "fahrenheit" | "F":
                        return "Det är " + str((languageModel.find_int(tokens) * 1.8) + 32) + " " + filteredtokens[1]
                    case "Kelvin" | "kelvin" | "K":
                        return "Det är " + str(languageModel.find_int(tokens) + 273.15) + " " + filteredtokens[1]
                    case "Rankine" | "rankine" | "R":
                        return "Det är " + str(languageModel.find_int(tokens) + 491.67) + " " + filteredtokens[1]
            case "Fahrenheit" | "fahrenheit" | "F":
                match filteredtokens[1]:
                    case "Celsius" | "celsius" | "C":
                        return "Det är " + str((languageModel.find_int(tokens) - 32) / 1.8) + " " + filteredtokens[1]
                    case "Kelvin" | "kelvin" | "K":
                        return "Det är " + str(((languageModel.find_int(tokens) - 32) / 1.8) - 273.15) + " " + filteredtokens[1]
                    case "Rankine" | "rankine" | "R":
                        return "Det är " + str(languageModel.find_int(tokens) + 459.67) + " " + filteredtokens[1]
            case "Kelvin" | "kelvin" | "K":
                match filteredtokens[1]:
                    case "Celsius" | "celsius" | "C":
                        return "Det är " + str(languageModel.find_int(tokens) - 273.15) + " " + filteredtokens[1]
                    case "Fahrenheit" | "fahrenheit" | "F":
                        return "Det är " + str(((languageModel.find_int(tokens) - 273.15) * 1.8) + 32) + " " + filteredtokens[1]
                    case "Rankine" | "rankine" | "R":
                        return "Det är " + str(languageModel.find_int(tokens) + 218.52) + " " + filteredtokens[1]
            case "Rankine" | "rankine" | "R":
                match filteredtokens[1]:
                    case "Celsius" | "celsius" | "C":
                        return "Det är " + str(languageModel.find_int(tokens) - 491.67) + " " + filteredtokens[1]
                    case "Fahrenheit" | "fahrenheit" | "F":
                        return "Det är " + str(languageModel.find_int(tokens) - 459.67) + " " + filteredtokens[1]
                    case "Kelvin" | "kelvin" | "K":
                        return "Det är " + str(languageModel.find_int(tokens) - 218.52) + " " + filteredtokens[1]
        return "Det är " + str(float(languageModel.find_int(tokens)) * (list_of_enhet[0]/list_of_enhet[1])) + " " + filteredtokens[1]