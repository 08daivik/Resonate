import faiss
import numpy as np

index = None
stored_chunks = []

# -------------------------------
# BUILD VECTOR STORE
# -------------------------------
def build_faiss(embeddings, chunks):
    global index, stored_chunks

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    stored_chunks = chunks


# -------------------------------
# RETRIEVE RELEVANT CHUNKS
# -------------------------------
def retrieve(query_vec, k: int = 5):
    global index, stored_chunks

    distances, indices = index.search(np.array([query_vec]), k)

    results = []
    for idx in indices[0]:
        results.append(stored_chunks[idx])

    return results
