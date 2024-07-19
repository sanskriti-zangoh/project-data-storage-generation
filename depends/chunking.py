from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title

def chunking_basic(elements):
    return chunk_elements(elements)

def chunking_title(elements):
    return chunk_by_title(elements)

