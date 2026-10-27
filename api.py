from fastapi import FastAPI
from pydantic import BaseModel

from retrieval import retrieve_documents
from generation import generate_answer


app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.post("/ask")
def ask_question(data: Question):

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_documents(
        data.question,
        top_k=3
    )

    # Generate answer using Qwen3
    answer = generate_answer(
        data.question,
        retrieved_chunks
    )

    return {
        "question": data.question,
        "answer": answer
    }