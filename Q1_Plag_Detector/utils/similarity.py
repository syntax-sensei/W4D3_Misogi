import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity_matrix(embeddings):
    sim_matrix = cosine_similarity(embeddings)
    return np.round(sim_matrix * 100, 2)

def find_clones(sim_matrix, threshold=80.0):
    n = sim_matrix.shape[0]
    clones = []
    for i in range(n):
        for j in range(i+1, n):
            if sim_matrix[i][j] >= threshold:
                clones.append((i, j, sim_matrix[i][j]))
    return clones
