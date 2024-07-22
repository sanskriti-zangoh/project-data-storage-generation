from unstructured.embed.openai import OpenAIEmbeddingEncoder, OpenAIEmbeddingConfig
from unstructured.embed.huggingface import HuggingFaceEmbeddingConfig, HuggingFaceEmbeddingEncoder
from unstructured.documents.elements import Element
import os
from dotenv import load_dotenv, find_dotenv
from typing import List

load_dotenv(find_dotenv())

openai_encoder = OpenAIEmbeddingEncoder(
    OpenAIEmbeddingConfig(
        api_key=os.getenv("OPENAI_API_KEY"),
))

hf_encoder = HuggingFaceEmbeddingEncoder(
    HuggingFaceEmbeddingConfig()
)

def create_document_embeddings_openai(chunks: List[Element])->List[Element]:
    return openai_encoder.embed_documents(chunks)

def create_query_embeddings_openai(queries: List[str]) -> List[List[float]]:
    return [openai_encoder.embed_query(query) for query in queries]

def create_document_embeddings_hf(chunks: List[Element]) -> List[Element]:
    return hf_encoder.embed_documents(chunks)

def create_query_embeddings_hf(queries: List[str])-> List[List[float]]:
    return [hf_encoder.embed_query(query) for query in queries]