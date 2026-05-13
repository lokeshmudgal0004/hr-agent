from langchain_community.vectorstores import FAISS

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store(documents):

    vector_db = FAISS.from_texts(
        documents,
        embedding_model
    )

    return vector_db