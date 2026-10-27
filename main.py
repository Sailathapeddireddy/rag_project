from ingest import ingest_pdf
from chunking import chunk_text
from embedding import create_embeddings
from vector_store import create_vector_store
from retrieval import retrieve_documents
from generation import generate_answer


def main():

    pdf_path = r"E:\GEN_AI\INDO-SAKURA_Employee_Handbook_2026_V1.1.pdf"

    # 1. Ingestion
    ingest_pdf(pdf_path)

    # 2. Chunking
    chunk_text()

    # 3. Embeddings
    create_embeddings()

    # 4. Vector store
    create_vector_store()

    # 5. Ask question
    question = input("\nEnter your question: ")

    # 6. Retrieval
    retrieved_chunks = retrieve_documents(question, top_k=3)

    # 7. Generate answer
    answer = generate_answer(question, retrieved_chunks)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()