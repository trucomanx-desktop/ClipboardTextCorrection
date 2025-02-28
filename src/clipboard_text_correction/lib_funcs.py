#!/usr/bin/python3

from gtts import gTTS
from playsound import playsound

import tempfile
from deep_consultation.core import consult_with_deepchat
import subprocess

RESPONSE=dict()
RESPONSE["<NOERROR>"] = "No errors was found"
RESPONSE["<ZERO>"]    = "ERROR! The output has zero length"
RESPONSE["<OK>"]      = "The query was resolved"


def play_message(texto, lang="en"):
    # Cria um arquivo temporário para o MP3
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        caminho_temp = temp_audio.name  # Obtém o caminho do arquivo temporário

    # Gera o áudio e salva no arquivo temporário
    tts = gTTS(texto, lang=lang)
    tts.save(caminho_temp)

    # Reproduz o áudio
    playsound(caminho_temp)



def comparar_textos(texto1, texto2, program="meld", filetype="txt"):
    """
    Compara dois textos utilizando um programa externo de comparação, como o Meld.
    
    Parâmetros:
    texto1 (str): Primeiro texto a ser comparado.
    texto2 (str): Segundo texto a ser comparado.
    program (str, opcional): Nome do programa de comparação de arquivos (padrão: "meld").
    filetype (str, opcional): Extensão do arquivo temporário a ser criado (padrão: "tex").
    
    Retorna:
    None: Apenas abre a ferramenta de comparação de arquivos.
    """
    # Cria arquivos temporários para armazenar os textos
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix="."+filetype) as temp1, \
         tempfile.NamedTemporaryFile(delete=False, mode="w", suffix="."+filetype) as temp2:
        
        temp1.write(texto1)
        temp2.write(texto2)
        
        temp1_path = temp1.name
        temp2_path = temp2.name

    # Executa o Meld sem bloquear a execução do script
    subprocess.Popen([program, temp1_path, temp2_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)




def consult_improve_writing(data,msg,program='meld'):

    SYSTEM_MSG='''
You are an expert system in text correction. Your task is to detect and correct errors in spelling, grammar, punctuation, coherence, and cohesion in any language.  

- If errors are found, return only a corrected version of the text, maintaining the original structure, line breaks, and formatting.  
- Make only the necessary changes, preserving the original meaning and tone.  
- Do not provide explanations, comments, or additional responses.  
- Do not translate or modify the language of the text.  
- If the text has no errors, return only "<NOERROR>". 
    '''
    
    OUT=consult_with_deepchat(data["base_url"],data["api_key"],data["model"],msg,SYSTEM_MSG)
    filetype="txt"

    if len(OUT)>0:
        if "<NOERROR>" in OUT or msg.strip()==OUT.strip():         
            return "<NOERROR>"

        comparar_textos(msg,OUT,program,filetype)
        return "<OK>"

    else:
        return "<ZERO>"
    
    return "<OK>"


def play_consult_return_message(msg):

    
    play_message(RESPONSE[msg])


