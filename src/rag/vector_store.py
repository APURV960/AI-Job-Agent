from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
index = None


def build_index(text_chunks):

    global index
    global documents

    embeddings = model.encode(text_chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    documents = text_chunks


def search(query, k=3):

    global index

    if index is None:
        raise RuntimeError(
            "Vector index not initialized. Run ingest_docs() first."
        )

    query_vector = model.encode([query])

    distances, indices = index.search(query_vector, k)

    results = []

    for i in indices[0]:
        results.append(documents[i])

    return results