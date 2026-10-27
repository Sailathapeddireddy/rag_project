import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def retrieve_documents(query, top_k=3):

    # Load FAISS vector store
    index = faiss.read_index("data/vector_store.index")

    # Load chunks
    with open("data/chunks.json", "r", encoding="utf-8") as file:
        chunks = json.load(file)

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Create embedding for user question
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    # Search FAISS
    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    # Get relevant chunks
    results = []

    for index_number in indices[0]:
        results.append(chunks[index_number]["text"])

    return results