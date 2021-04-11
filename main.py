import requests
import json
from bs4 import BeautifulSoup
import re
import tweepy


def tweet(fact):
    with open('credential.json') as json_file:
        data = json.load(json_file)
        consumer_key = data['consumer_key']
        consumer_secret = data['consumer_secret']
        access_token = data['access_token']
        access_token_secret = data['access_token_secret']


    twitter_auth_keys = { 
        "consumer_key"        : consumer_key,
        "consumer_secret"     : consumer_secret,
        "access_token"        : access_token,
        "access_token_secret" : access_token_secret
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    tweet = fact
    status = api.update_status(status=tweet) 




def is_at_least_a_10_words_sentence(p) :
    # sentence needs to be at least 10 words
    if len(p.split()) < 10 :
        return False
    else :
        return True

def is_not_full_of_number(p) :
    # sentence needs to be composed by a maximum of 20% digits
    if sum(c.isdigit() for c in p * 100) / len(p) > 20  :
        return False
    else :
        return True

def is_not_a_wikipedia_recommendation(p) :
    # sentence isn't part of wikipedia recommendation
    recommendations = [
        "Vous pouvez partager vos connaissances",
        "Si vous disposez d'ouvrages ou d'articles de référence",
        "Quelles sources sont attendues",
        "modifier - modifier le code"
        ]
    for reco in recommendations :    
        if reco in p :
            return False
    return True

def is_a_good_paragraph(p) :
    if is_at_least_a_10_words_sentence(p) and is_not_full_of_number(p) and is_not_a_wikipedia_recommendation(p) :
        return True
    else :
        return False

def clean_fact(p):
    # removing the content between parentheses (whatever)
    # ISSUE : there's sometimes parenthese within parethese #parentheception #(what(thefuck))
    # https://fr.wikipedia.org/wiki/Pierre_Oudaille
    p=(re.sub(r" ?\([^)]+\)", "", p))
    # removing notes between square brackets [whatever]
    p=(re.sub(r" ?\[[^)]+\]", "", p))
    return p


def get_fact_from_random_wiki_page() :
    response = requests.get('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')    
    # response = requests.get('https://fr.wikipedia.org/wiki/Best_~Third_Universe~_/_Universe')
    # response = requests.get('https://fr.wikipedia.org/wiki/Zaldu')
    print(response.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_paragraphs = soup.find("div", {"id":"mw-content-text"}).findAll('p')
    if len(all_paragraphs) != 0 :
        for p in all_paragraphs:
            if is_a_good_paragraph(p.text) :
                return clean_fact(p.text)
            elif p == all_paragraphs[-1] :                    
                get_fact_from_random_wiki_page()
            else :
                continue
    else :
        get_random_wiki_page()



tweet(get_fact_from_random_wiki_page())