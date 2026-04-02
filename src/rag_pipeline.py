from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vector_store(texts):
    # Combine all text
    full_text = "\n".join([t for t in texts if t])

    if not full_text.strip():
        raise ValueError("No text extracted from PDFs")

    # Split text
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_text(full_text)

    # Remove empty chunks
    docs = [d for d in docs if d.strip()]

    if not docs:
        raise ValueError("No valid text chunks created")

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector DB
    db = Chroma.from_texts(docs, embeddings)

    return db


def query_docs(db):
    docs = db.similarity_search("building defects moisture cracks leakage thermal issues", k=5)

    return "\n".join([doc.page_content for doc in docs])