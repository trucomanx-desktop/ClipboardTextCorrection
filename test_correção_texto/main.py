#!/usr/bin/python3
import json

with open("/home/fernando/apikey.json", "r") as arquivo:
    config_apikey = json.load(arquivo)


MSG='''Pelo que se observa, 
a palavra ``batuque'' não se usava para se referir a uma dança em particular mas sim aos festejos dos negros em geral \cite[pp. 85]{sandroni2001feitico}.
'''
API_KEY=config_apikey["API_KEY_DEEPINFRA"]

BASE_URL="https://api.deepinfra.com/v1/openai"

MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"


import deep_consult as cdi

cdi.consult_with_deepinfra(BASE_URL,API_KEY,MODEL,MSG)
