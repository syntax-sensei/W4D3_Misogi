import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text.strip())
    return text
