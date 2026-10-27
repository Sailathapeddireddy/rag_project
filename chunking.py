import json
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text():

    input_path = Path("data/extracted_text.txt")
    output_path = Path("data/chunks.json")

    # Read extracted text
    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Create text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Create chunks
    chunks = text_splitter.split_text(text)

    # Store chunks
    chunk_data = []

    for i, chunk in enumerate(chunks):

        chunk_data.append({
            "chunk_id": i,
            "text": chunk
        })

    # Save chunks as JSON
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            chunk_data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Chunks created: {len(chunks)}")
    print(f"Chunks saved to: {output_path}")

    return chunk_data