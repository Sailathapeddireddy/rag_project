import numpy as np
import faiss


def create_vector_store():

    # Load embeddings
    embeddings = np.load("data/embeddings.npy")

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])

    # Add embeddings to index
    index.add(embeddings.astype("float32"))

    # Save FAISS index
    faiss.write_index(index, "data/vector_store.index")

    print(f"Vectors added: {index.ntotal}")
    print("Vector store saved to data/vector_store.index")

    return index