from encodings.punycode import generate_generalized_integer

import ui
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import Registration
from Registration import RegVar

anvandningar_lista = {
    "registrera för prova på dag": ["prova",],
    "FAQ": ["antagning","program","prov","kurs", "lektion",],
    "SL-kort": ["SL", "bus", "tåg", "pendel"],
    "IND-val": ["ind", "individuella val"],
    "Bibliotek":["bibliotek", "böker"]
    

}

#måste finnas minst 3 svarsmöjligheter per lista annars kommer random choice bara välja den andra svarsmöjligheten
svars_lista = {
    "FAQ": [
        "Vi förstår att du kan ha specifika frågor som behöver hjälp. Besök vår hemsida för att få tillgång till våra supporttjänster eller kontakta oss direkt för personlig assistans på tumbagymnasium.se",
        "Om du har specifika frågor, besök vår hemsida för information om våra program och andra resurser, eller använd kontaktsidan på tumbagymnasium.se för att nå vår personal direkt.",
        "Behöver du hjälp med frågor? På vår hemsida hittar du information om vilka program vi erbjuder, och du kan också kontakta vår personal direkt via kontaktsidan på tumbagymnasium.se."
    ],
    "registrera för prova på dag": [
        "du kan nu skriva in namn och mailadress så kan vi kontakta dig för att prova på en dag hos oss",
        "kul att du vill anmäla dig till en prova på dag, skriv nu ditt namn och mejladress så vi kan kontakta dig",
        "tack för ditt intresse för att prova på en dag hos tumba gymnasium, skriv nu ned ditt namn och mejladress så kontaktar vi dig"
    ],
    "SL-kort": [
        """Undrar du om hur skolan erbjuder Sl-kort? detta kan var några saker att veta:

SL-kort (skolkort) är du berättigad till om din folkbokföringsadress är mer än 6 km från din skola och du är under 20 år. Vi mäter avståndet via google maps (gångväg)

VANLIGA FRÅGOR

Hur får jag mitt kort?

Du köper ett kort på pressbyrån (20 kr). Värdekoden som skall tankas på kortet mejlas till elevens skolmejl.

När gäller kortet?

Kortet gäller varje vardag (måndag till fredag) mellan 04:30 och 19:00

Vad händer om jag tappar bort mitt kort?

För att ha gällande förlustgaranti så är det viktigt att registrera det Gröna kortet på SL:S hemsida. För att registrera kortet för förlustgaranti behöver du ha fyllt 16 år och ha BankID, är du under 16 år kan vårdnadshavare registrera kortet. Om du saknar BankID kan du få hjälp att registrera kortet hos våra kundtjänstbutiker på Sergels torg och Stockholms central."""
    ],
    "IND-val": [ 
        """Undrar du hur många IND-val kurser vi har har på tumba? har finns litte information om vårt sortiment.
Tumba Gymnasium är en stor skola med många olika program därför kan vi erbjuda ett stort utbud av IND- val.

Här följer en del exempel:

• Moderna språk steg 1,2,3,4 och 5
• Estetiska kurser så som bild, foto, film, scenisk gestaltning, radio, fotografi, körsång och dans.
• Webbutveckling, webdesign, E-sport och programmering
• Entreprenörskap och retorik
• Idrottskurser så som friskvård, tjejidrott, fotboll, TG Toughest m.m
• Engelska 7dfg
• Matematik 2,3,4 och 5
• Beteendevetenskapliga kurser så som kriminologi, psykologi och sociologi """
    ],
    "Bibliotek": [ 
        """Undrar du något om biblioteket i tumba?

 Biblioteket - skolans hjärta
TG har Södertörns största gymnasiebibliotek. Det är en oas där du både kan grupparbeta
och studera enskilt. Vi har massor av bra böcker och bibliotekets personal hjälper dig
hitta rätt både i biblioteket och bland webbens alla infomationsresurser.

Öppettider:
Må 08.00-16.00 (studiepass 16.00-17.00)
Ti 10.00-16.00 (mattestöd 09.00-10.00, studiepass 16.00-17.00)
On 08.00-15.00
To 08.00-16.00 (studiepass 16.00-17.00)
Fr 08.00-14.30"""
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
        return ("Ber om ursäkt, men jag kan inte hjälpa dig med det. Jag kan hjälpa dig med att registrera för prova på dagar eller kanske har du andra frågor om skolan?")

def detection_func(user_input, inputuser):
    if Registration.RegVar == False:
        issue_category = detect_issue(user_input)
        if issue_category == "registrera för prova på dag":
            Registration.RegFunc(str(inputuser))
        response = generate_response(issue_category)
        return response
    else:
        Registration.RegFunc(str(inputuser))
        return "Tack för din ansökan!"