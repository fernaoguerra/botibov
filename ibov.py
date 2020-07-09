import yfinance as yf
from pprint import pprint
import random

def get_ibov_answer():
    ibov = yf.Ticker("%5EBVSP")
    # pprint (ibov.info)
    dayHigh = ibov.info['dayHigh']
    dayLow = ibov.info['dayLow']
    print ("minínima " + str(dayLow))
    print ("Máxima " + str(dayHigh))
    data = ibov.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print(ibov,last_quote)
    
    tweet1 = ("Festa dos 100k?\n"+ \
        "Ibovespa agora: " + str(last_quote) + "\n" + \
        "Miníma do dia: " + str(dayLow) + "\n" + \
        "Máxima do dia: " + str(dayHigh) + "\n" + \
        "Para receber updates do Ibov é só me marcar em tweets")
    
    tweet2 = ("Você recebeu esse tweet porque digitou 'ibov'.\n"+ \
        "Ibovespa agora: " + str(last_quote) + "\n" + \
        "Miníma do dia: " + str(dayLow) + "\n" + \
        "Máxima do dia: " + str(dayHigh) + "\n" \
        "Me marca para receber updates do Ibov")
    
    tweet3 = ("Você recebeu esse tweet porque mencionou o Ibov.\n"+ \
        "Ibovespa agora: " + str(last_quote) + "\n" + \
        "Miníma do dia: " + str(dayLow) + "\n" + \
        "Máxima do dia: " + str(dayHigh) + "\n"+  \
        "Para receber updates do Ibov é só me marcar em tweets")
    
    tweet_list = [tweet1,tweet3,tweet3]
    random_tweet = (random.choice(tweet_list)) 
    print (random_tweet)
    return random_tweet

# get_ibov_answer()