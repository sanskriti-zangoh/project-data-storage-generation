import faiss
import numpy as np
from unstructured.documents.elements import Element
from typing import List

def add_index(elements: list[Element]):
    # Add all elements to faiss index
    # TODO: use an in-memory index
    dimension = len(elements[0].to_dict()['embeddings'])
    print(f"dimension: {dimension}")
    index = faiss.IndexFlatL2(dimension)
    embeddings = np.array([e.to_dict()['embeddings'] for e in elements], dtype=np.float32)
    index.add(embeddings)
    return index

def search_index(index: faiss.IndexFlatL2, query_embeddings: list[list[float]], k: int = 3):
    # TODO: use an in-memory index
    query_embeddings = np.array(query_embeddings, dtype=np.float32)  # Ensure the query embeddings are in the correct format
    indices = []
    for embedding in query_embeddings:
        embedding = np.array(embedding).reshape(1, -1)  # Convert to NumPy array and reshape to 2D array
        D, I = index.search(embedding, k)
        indices.append(I[0].tolist())  # Convert to a list
    return indices

def doc_retrival_from_indices(indices: list[list[int]], elements: list[Element]):
    # TODO: use an in-memory index
    answer_elements = []
    for i in range(len(indices)):
        print(f"Query {i}:")
        answer_elements_query = []
        for j in indices[i]:
            print(f"- {elements[j].to_dict()['text']}")
            answer_elements_query.append(elements[j])
        print()
        answer_elements.append(answer_elements_query)
    return answer_elements