import requests


def generate_answer(question, retrieved_chunks):

    # System prompt
    system_prompt = """
You are a helpful RAG chatbot.

Answer the user's question using only the provided context.
If the answer is not available in the context, say:
"I don't know based on the provided document."

Do not make up information.
Keep the answer simple and clear.
"""

    # Combine retrieved chunks
    context = "\n\n".join(retrieved_chunks)

    # User prompt
    user_prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    # Send request to Ollama
    response = requests.post(
        "http://host.docker.internal:11434/api/chat",
        json={
            "model": "qwen3:4b",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "stream": False
        }
    )

    result = response.json()

    return result["message"]["content"]