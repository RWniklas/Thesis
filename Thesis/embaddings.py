import openai 
import ast
import os 
import pandas as pd
import numpy as np
from getpass import getpass
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
from ai import *
from library import *
import math

OPENAI_KEY = "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"

MODEL = "text-embedding-ada-002"
openai.api_key = OPENAI_KEY


   

    

    

def create_chunk(string):
    text = string.strip()
    words = len(text.split())
    words_l = text.split()
    n_chuncks =  math.ceil(words / 250)
    desired_word_count = math.ceil(words / n_chuncks)
    substrings = []
    current_substring = ""

    for word in words_l:
        if len(current_substring.split()) < desired_word_count:
            current_substring += word + " "
        else:
            substrings.append(current_substring.strip())
            current_substring = word + " "
    
    substrings.append(current_substring.strip())

    return pd.DataFrame(substrings,columns=['text'])
    
    
    


def create_embadding(file,name=""):
    if type(file) == str:
        return get_embedding(file,engine=MODEL)
    

    if os.path.splitext(file.name)[-1].lower() == ".txt":

        with open(file.name, encoding="utf-8") as f:
            content = f.read()
            df = create_chunk(content)
            

    if os.path.splitext(file.name)[-1].lower() =="xlsx":
        df  = pd.read_excel(file.name)

    df =pd.read_excel(file.name)
    new_df = pd.DataFrame(columns=["embedding"])
    count= 0
    for i,r in df.iterrows():
        count += 1
        emb = get_embedding(r["text"], engine=MODEL)
        new_df.loc[i] = [emb]
    final_df = pd.concat([df, new_df], axis=1)
    final_df.to_csv(f"data/{name}.csv",mode='w')
    return f"{count} new unique chunks are created"


def query_search(question,K,libraries):
    
    query_vector = create_embadding(question)
    result  = similarity(query_vector,libraries,K)
   
    
    
    answer = api_question(result,question)


    return answer,result
    





def similarity(query_vector,libraries,K):
    conc_df = pd.DataFrame({'text': [], 'similarities': []})
    for lib in libraries:
        df = pd.read_csv(f"data/{lib}")
        df['embedding'] = df['embedding'].apply(ast.literal_eval)
        df["similarities"] = df["embedding"].apply(lambda x: cosine_similarity(x,query_vector))
        conc_df = pd.concat([conc_df,df[["text","similarities"]]],ignore_index=True)

    sorted_rows = conc_df.nlargest(K, 'similarities')  
    result = sorted_rows[['text']].values.tolist()

    return result
