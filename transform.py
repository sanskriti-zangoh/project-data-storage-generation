"""
Transforms unstructured data to structured data.
"""

from unstructured.partition.auto import partition

def generate_elements(filename):
    return partition(filename=filename)