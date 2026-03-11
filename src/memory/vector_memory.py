from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")

memory_vectors = []


def store_vector(text):

    embedding = model.encode(text)

    memory_vectors.append(embedding)

    return embedding


def search_memory(query):

    query_embedding = model.encode(query)

    similarities = []

    for vec in memory_vectors:

        score = np.dot(query_embedding, vec)

        similarities.append(score)

    return similarities