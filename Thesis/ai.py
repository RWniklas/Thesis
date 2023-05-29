import openai
import pandas as pd


OPENAI_KEY = "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"
MODEL = "gpt-3.5-turbo"
openai.api_key = OPENAI_KEY

def message_constructor(base,context):
   
    print(len(context))
    for el in context: 
        base.insert(1,{"role": "user", "content":f"{el}"})
   
    return base

def api_question(context,question): 
    completion= openai.ChatCompletion.create(
        model=MODEL,
        messages =  message_constructor([
        {"role": "system", "content":"Your are an Question Asnwer assistent. I will provide you with information. Based on the try to answer the question i ask you. "},
        
        {"role": "user", "content": f"Based on the information i provided to you. Asnwer this Question: {question} "}

        ],context)


    )
    return completion["choices"][0]["message"]["content"]



