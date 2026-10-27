from langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path


def ingest_pdf(pdf_path):

    # Load PDF using LangChain
    loader = PyMuPDFLoader(pdf_path)

    documents = loader.load()

    # Store extracted text
    extracted_text = ""

    for document in documents:
        extracted_text += document.page_content
        extracted_text += "\n\n"

    # Create data folder if it doesn't exist
    output_folder = Path("data")
    output_folder.mkdir(exist_ok=True)

    # Save extracted content as TXT
    output_path = output_folder / "extracted_text.txt"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print(f"Pages loaded: {len(documents)}")
    print(f"Extracted text saved to: {output_path}")

    return documents