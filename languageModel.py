from encodings.punycode import generate_generalized_integer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import Registration
import Primtal
import Programs


anvandningar_lista = {
    "registrera för prova på dag": ["prova","testa", "registrera", "anmäla"],
    "SL-kort": ["SL", "bus", "tåg", "pendel", "sl"],
    "IND-val": ["ind", "individuella", "IND"],
    "Bibliotek":["bibliotek", "böcker", "biblioteket"],
    "mat": ["skolmat", "matsal", "mat", "skolmaten", "lunch", "skollunch", "maten"],
    "program": ["teknik","antagning", "program","programmet","kurser", "kurs", "data", "programmering", "programera", "arkitektur", "design", "teknikvetenskap", "medieteknik", "inriktningar", "linjer", "linje", "linjen", "linjerna","it", "IT"],
    "merit": ["merit", "medelmerit", "betyg", "medelbetyg", "antagningsgräns", "antagning", "gräns", "median", "medelantagning", "poäng", "meritpoäng"],
    "plugg": ["tufft", "studier", "plugg", "plugga"],
    "sporter":["handboll", "hockey", "NIU", "LIU", "niu", "liu"],
    "när gäller kortet?": ["gäller"],
    "hur får jag mitt kort?": ["kort"],
    "procent tjejer": ["tjejer", "tjej", "procent", "andel", "procentet", "andelen"],
    "1974":["gammal", "årtal", "jubeleum", "jubeleumet"],
    "FAQ": ["prov","examination","examinationer", "lektion", "schema", "schemat", "scheman", "termin", "terminen", "ligger", "elever", "elev","datorer", "lånedator", "dator", "lånedatorer", "klass", "klassen", "klasser", "elever", "tg", "tumba", "Tumba", "lärare", "lärarna", "raster"],
    "hälsning":["hej", "goddag","tjena","tja","tjenare","halloj", "Hej", "Goddag", "Tjena", "Tja", "Tjenare", "Halloj", "tjo", "Tjo"],
    "vad händer om jag tappar bort mitt kort": ["tappar"],
    "Tack": ["Tack", "tack"],
    "Rektor": ["Rektor", "rektor", "rektorn", "alf", "Alf"]
}


svars_lista = {
    "FAQ": [
        "Jag förstår att du kan ha specifika frågor som du behöver hjälp med. Fråga en av eleverna eller lärarna i närheten!",
        "Jag kan inte hjäpa med allt. Fråga en av eleverna eller lärarna i närheten, de kan svara på det mesta!",
        "Jag kan inte svara på den frågan men jag kan anmäla dig till en prova på dag!"
    ],
    "registrera för prova på dag": [
        "Du kan nu skriva in förnamn, efternamn och mejladress så kan vi kontakta dig för att prova på en dag hos oss",
        "Kul att du vill anmäla dig till en prova på dag, skriv nu ditt förnamn, efternamn och mejladress så vi kan kontakta dig",
        "Tack för ditt intresse för att prova på en dag hos tumba gymnasium, skriv nu ned ditt förnamn, efternamn och mejladress så kontaktar vi dig"
    ],
     "hälsning":[
        "Goddag, vad skulle du vilja veta om tumba gymnasium? Jag kan hjälpa med att registrera dig för en prova på dag också 😊 "
    ],
    "hur får jag mitt kort?":[
        "Om du bor tillräckligt långt bort kommer du få ett brev hem i brevlådan med ett SL-kort och en värdekod"
    ],
    "när gäller kortet?":[
        "Kortet gäller varje vardag (måndag till fredag) mellan 04:30 och 19:00."
    ],
    "SL-kort": [
        """Undrar du om hur skolan erbjuder Sl-kort? Detta kan vara några saker att veta:

SL-kort (skolkort) är du berättigad till om din folkbokföringsadress är mer än 6 km från din skola och du är under 20 år. Vi mäter avståndet via google maps (gångväg)

VANLIGA FRÅGOR

Hur får jag mitt kort?

När gäller kortet?

Vad händer om jag tappar bort mitt kort?"""
],
     "IND-val": [ 
        """Undrar du hur många IND-val kurser vi har har på tumba? har finns litte information om vårt sortiment.
Tumba Gymnasium är en stor skola med många olika program därför kan vi erbjuda ett stort utbud av IND- val.

Några exempel:

• Moderna språk steg 1,2,3,4 och 5
• Estetiska kurser så som bild, foto, film, scenisk gestaltning, radio, fotografi, körsång och dans.
• Webbutveckling, webdesign, E-sport och programmering
• Entreprenörskap och retorik
• Idrottskurser så som friskvård, tjejidrott, fotboll, TG Toughest m.m
• Engelska 7
• Matematik 5
• Beteendevetenskapliga kurser så som kriminologi, psykologi och sociologi """
    ],
    "Bibliotek": [ 
        """TG har Södertörns största gymnasiebibliotek. Det är en oas där du både kan grupparbeta
och studera enskilt. Vi har massor av bra böcker och bibliotekets personal hjälper dig
hitta rätt både i biblioteket och bland webbens alla infomationsresurser.

Öppettider:
Må 08.00-16.00 (studiepass 16.00-17.00)
Ti 10.00-16.00 (mattestöd 09.00-10.00, studiepass 16.00-17.00)
On 08.00-15.00
To 08.00-16.00 (studiepass 16.00-17.00)
Fr 08.00-14.30"""
        ],
    "mat": ["Skolmaten är både god och varierad. Om du vill testa den kan du anmäla dig till en prova på dag genom mig. Då kommer du kunna uppleva en hel dag som teknik elev, inklusive skolmaten!"],
    "procent tjejer": ["Teknikprogrammet består av ungefär 30% tjejer, detta har ökat med varje år som går."],
    "program": [" På teknikprogrammet har vi fyra inriktningar. De är teknikvetenskap, design- och produktutveckling, samhällsbyggande och miljö samt informations- och medieteknik. Om du har vidare frågor om dessa inriktningar fråga gärna eleverna eller lärarna i närheten."],
    "merit": ["Antagninggränsen för teknikprogrammen var på 272.5-290, beroende på inriktning, vill du ha mer specifik information kan du kolla tumba gymnasiums websida eller fråga eleverna och lärarna i närheten."],
    "vad händer om jag tappar bort mitt kort":[
        "För att ha gällande förlustgaranti så är det viktigt att registrera det Gröna kortet på SL:S hemsida. För att registrera kortet för förlustgaranti behöver du ha fyllt 16 år och ha BankID, är du under 16 år kan vårdnadshavare registrera kortet. Om du saknar BankID kan du få hjälp att registrera kortet hos SLs kundtjänstbutiker på Sergels torg och Stockholms central."
    ],
    "sporter":["Är du intresserad av våra NIU eller LIU program finns det elever och lärare tillgängliga som kan berätta mer information om de. Ifall du inte vet vart du ska hitta de, fråga gärna eleverna eller lärarna i närheten."],
    "plugg":["Mängden du behöver plugga eller hur tufft du upplever programmet beror på många faktorer, därför kan jag inte ge dig ett konkret svar. Rekommenderar att prata med våra elever som är här på öppethus för att se deras perspektiv. Jag kan hjälpa dig med att anmäla dig till prova på dag, detta kan hjälppa dig genom att du då får uppleva en dag av studier med våra teknikelever."],
    "1974":["Tumba gymnasium grundades 1974, vi fyller 50 år!"],
    "Tack": ["Inga problem! Finns det något mer jag kan hjälpa med?"],
    "Rektor": ["Alf Solander är vår GUD! Vi bönfaller honom varje måltid och tackar honom för allt han gjort för Tumba gymnasium!"]
    }

def find_int(tokens):
    for i in tokens:
        if i.isdigit() == True:
            return i



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
        return ("Ber om ursäkt, men jag kan inte hjälpa dig med det. Kolla din stavning eftersom jag inte fattar stavfel. Jag kan hjälpa dig med att registrera för prova på dagar eller kanske har du andra frågor om skolan?")

def detection_func(user_input):
    if Registration.RegVar == False:
        issue_category = detect_issue(user_input)
        if issue_category == "registrera för prova på dag":
            Registration.RegFunc(str(user_input), issue_category)
        response = generate_response(issue_category)
        return response
    else:
        Registration.RegFunc(str(user_input))
        return "Tack för din ansökan!"

def match_case(user_input):
    tokens = user_input.split()
    for i in tokens:
        match i:
            case "primtalet":
                print("tokens", tokens, " int", (find_int(tokens)))
                return Primtal.primtal_calc(int(find_int(tokens)))
            case "rövarspråk,":
                print("tokens", tokens)
                return Programs.rövarspråk(user_input)
            case _:
                print("tokens", tokens,)
                return detection_func(user_input)
