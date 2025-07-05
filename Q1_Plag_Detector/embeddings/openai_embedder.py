import os
import openai
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIEmbedder:
    def __init__(self, model='text-embedding-3-small'):
        self.model = model
    
    def get_embeddings(self, texts):
        response = openai.embeddings.create(model=self.model, input=texts)
        return np.array([r.embedding for r in response.data])
