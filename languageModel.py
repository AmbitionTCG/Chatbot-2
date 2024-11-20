from encodings.punycode import generate_generalized_integer

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import Registration
from Registration import RegVar

anvandningar_lista = {
    "registrera för prova på dag": ["prova",],
    "FAQ": ["antagning","program","prov","kurs", "lektion",]

}

#måste finnas minst 3 svarsmöjligheter per lista annars kommer random choice bara välja den andra svarsmöjligheten
svars_lista = {
    "FAQ": [
        "Vi förstår att du kan ha specifika frågor som behöver hjälp. Besök vår hemsida för att få tillgång till våra supporttjänster eller kontakta oss direkt för personlig assistans på tumbagymnasium.se",
        "Om du har specifika frågor, besök vår hemsida för information om våra program och andra resurser, eller använd kontaktsidan på tumbagymnasium.se för att nå vår personal direkt.",
        "Behöver du hjälp med frågor? På vår hemsida hittar du information om vilka program vi erbjuder, och du kan också kontakta vår personal direkt via kontaktsidan på tumbagymnasium.se."
    ],
    "registrera för prova på dag": [
        "Är du intresserad av att testa på en dag hos Tumba Gymnasium vid nästa 'prova på'-tillfälle?",
        "Nyfiken på hur det är att gå på Tumba Gymnasium? Delta i vårt kommande 'prova på'-tillfälle!",
        "Du kan prova på hos Tumba Gymnasium vid vårt nästa 'prova på'-tillfälle."
    ]
}
#preprocess user input
def preprocess_input(user_input):
    tokens = word_tokenize(user_input)
    stop_words = set(stopwords.words('swedish'))
    filtered_tokens =[word for word in tokens if word not in stop_words]
    return filtered_tokens


def detect_issue(user_input):
    tokens = preprocess_input(user_input)

    for category, keywords in anvandningar_lista.items():
        if any(keyword in tokens for keyword in keywords):
            return category
    return "general"

def generate_response(issue_category):
    if issue_category in svars_lista:
        return random.choice(svars_lista[issue_category])
    else:
        return ("Ber om ursäkt, men jag kan inte hjälpa dig med det.")

def detection_func(user_input):
    if RegVar == False:
        issue_category = detect_issue(user_input)
        if issue_category == "registrera för prova på dag":
            Registration.RegFunc()
        response = generate_response(issue_category)
        return response

