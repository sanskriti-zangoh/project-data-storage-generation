from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import Element

def chunking_basic(elements: list[Element]):
    return chunk_elements(elements)

def chunking_title(elements: list[Element]):
    return chunk_by_title(elements)

