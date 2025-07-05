import re
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Semantic chunking by merging similar sentences

def semantic_chunk(text, max_words=150):
    # Simple sentence splitting using regex
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    embeddings = model.encode(sentences, convert_to_tensor=True)

    chunks = []
    current_chunk = []
    current_len = 0

    for i, sent in enumerate(sentences):
        sent_len = len(sent.split())
        if current_len + sent_len > max_words:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [sent]
            current_len = sent_len
        else:
            if current_chunk:
                sim = util.cos_sim(model.encode(sent, convert_to_tensor=True), model.encode(current_chunk[-1], convert_to_tensor=True))
                if sim.item() < 0.3:  # Semantic break
                    chunks.append(' '.join(current_chunk))
                    current_chunk = [sent]
                    current_len = sent_len
                    continue
            current_chunk.append(sent)
            current_len += sent_len

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks