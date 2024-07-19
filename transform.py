"""
Transforms unstructured data to structured data.
"""

from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf

def generate_elements(filename):
    return partition(filename=filename)

def generate_pdf_hi_res(filename):
    return partition_pdf(
    filename=filename,                                     # mandatory
    strategy="hi_res",                                     # mandatory to use ``hi_res`` strategy
    extract_images_in_pdf=True,                            # mandatory to set as ``True``
    extract_image_block_types=["Image", "Table"],          # optional
    extract_image_block_to_payload=False,                  # optional
    extract_image_block_output_dir="save",  # optional - only works when ``extract_image_block_to_payload=False``
)
