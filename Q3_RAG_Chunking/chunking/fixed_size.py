def chunk_by_chars(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]

def chunk_by_words(text, size):
    words = text.split()
    return [' '.join(words[i:i+size]) for i in range(0, len(words), size)]