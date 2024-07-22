from unstructured.embed.openai import OpenAIEmbeddingEncoder, OpenAIEmbeddingConfig
from unstructured.embed.huggingface import HuggingFaceEmbeddingConfig, HuggingFaceEmbeddingEncoder
from unstructured.documents.elements import Element
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai_encoder = OpenAIEmbeddingEncoder(
    OpenAIEmbeddingConfig(
        api_key=os.getenv("OPENAI_API_KEY"),
))

hf_encoder = HuggingFaceEmbeddingEncoder(
    HuggingFaceEmbeddingConfig()
)

def create_document_embeddings_openai(chunks: list[Element]):
    return openai_encoder.embed_documents(chunks)

def create_query_embeddings_openai(queries: list[str]):
    return [openai_encoder.embed_query(query) for query in queries]

def create_document_embeddings_hf(chunks: list[Element]):
    return hf_encoder.embed_documents(chunks)

def create_query_embeddings_hf(queries: list[str]):
    return [hf_encoder.embed_query(query) for query in queries]