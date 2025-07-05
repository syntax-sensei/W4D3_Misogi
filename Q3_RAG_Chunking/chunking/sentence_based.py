import re

def chunk_by_sentences(text, max_words):
    # Simple sentence splitting using regex
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    chunks = []
    current_chunk = []
    word_count = 0

    for sent in sentences:
        words = sent.split()
        if word_count + len(words) <= max_words:
            current_chunk.append(sent)
            word_count += len(words)
        else:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [sent]
            word_count = len(words)

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
