import json
import numpy as np
from sentence_transformers import SentenceTransformer


def create_embeddings():

    # Read chunks
    with open("data/chunks.json", "r", encoding="utf-8") as file:
        chunks = json.load(file)

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Get text from chunks
    texts = [chunk["text"] for chunk in chunks]

    # Create embeddings
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    # Save embeddings
    np.save("data/embeddings.npy", embeddings)

    print(f"Embeddings created: {len(embeddings)}")
    print(f"Embedding size: {embeddings.shape[1]}")
    print("Embeddings saved to data/embeddings.npy")

    return embeddings