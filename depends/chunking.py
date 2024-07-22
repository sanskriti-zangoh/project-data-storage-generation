from unstructured.chunking.basic import chunk_elements
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import Element
from typing import List

def chunking_basic(elements: List[Element])-> List[Element]:
    return chunk_elements(elements)

def chunking_title(elements: List[Element]) -> List[Element]:
    return chunk_by_title(elements)

