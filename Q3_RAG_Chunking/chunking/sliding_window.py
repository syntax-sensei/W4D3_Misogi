def chunk_with_overlap(text, size, overlap):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + size, len(words))
        chunks.append(' '.join(words[start:end]))
        start += size - overlap

    return chunks