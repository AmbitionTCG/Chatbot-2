from encodings.punycode import generate_generalized_integer

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

anvandningar_lista = {
    "Stuff1": ["1Stuff"],
    "Stuff2": ["2Stuff"]
}

svars_lista = {
    "sak1": [
        "Svarsmöjlighet 1.1"
        "svarsmöjlighet 1.2"
    ],
    "sak2": [
        "Svarsmöjlighet 2.1"
        "Svarsmöjlighet 2.2"
    ]
}
#preprocess user input
def preprocess_input(user_input):
    tokens = word_tokenize(user_input)
    stop_words = set(stopwords.words('english'))
    filtered_tokens =[word for word in tokens if word not in stop_words]
    return filtered_tokens


def detect_issue(user_input):
    tokens = preprocess_input(user_input)

    for category, keywords in anvandningar_lista.item():
        if any(keyword in tokens for keyword in keywords):
            return category
    return "general"

def generate_response(issue_category):
    if issue_category in svars_lista:
        return random.choice(responses[issue_category])
    else:
        return ("Ber om ursäkt, men kan inte hjälpa dig med det.")

#hur functionerna skulle funka
    """"issue_category = detect_issue(user_input)

    response = generate_response(issue_category)

    print(response)"""
