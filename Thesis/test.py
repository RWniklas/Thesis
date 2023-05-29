import pandas as pd
from openai.embeddings_utils import cosine_similarity
import openai 
from openai.embeddings_utils import get_embedding
import ast
OPENAI_KEY = "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"

MODEL = "text-embedding-ada-002"
openai.api_key = OPENAI_KEY

df = pd.read_csv("embeddings.csv")
df['embedding'] = df['embedding'].apply(ast.literal_eval) #let col wit list read correctly

sorted_df = df.sort_values(by="embedding", inplace=True)

print(sorted_df)