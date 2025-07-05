def explain_strategy(strategy):
    if strategy == "Fixed Size (Characters)":
        return "Splits text into equal-sized character chunks. Simple and fast but may break context."
    elif strategy == "Fixed Size (Words)":
        return "Splits text by word count. Maintains better boundaries than characters."
    elif strategy == "Sentence Based":
        return "Uses NLP to chunk by sentence boundaries, grouping up to a word limit."
    elif strategy == "Sliding Window with Overlap":
        return "Maintains overlapping chunks for better retrieval performance."
    elif strategy == "Semantic Chunking":
        return "Uses sentence embeddings to group semantically similar sentences together. Creates more coherent chunks based on meaning."
    else:
        return "Unknown strategy."