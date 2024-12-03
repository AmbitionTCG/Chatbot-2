def hitta_enheter(tokens):
    
    enheter = [
    "Centimeter", "cm", "Meter", "m", "Kilometer", "km", "Millimeter", "mm", 
    "Tum", "in", "Fot", "ft", "Yard", "yd", "Mile", "mi",
    
    "Gram", "g", "Kilogram", "kg", "Ton", "t", "Milligram", "mg", 
    "Ounce", "oz", "Pound", "lb", "Stone", "st",
    
    "Liter", "l", "Milliliter", "ml", "Kubikmeter", "m³", 
    "Kubikcentimeter", "cm³", "Cubic inch", "in³", "Gallon", "gal", 
    "Quart", "qt", "Pint", "pt", "Cup", "cup", ,
    
    "Celsius", "°C", "Fahrenheit", "°F", "Kelvin", "K", "Rankine", "°R"
]
    output = []
    for i in tokens:
        if i in enheter:
            output.append(i)
    return output