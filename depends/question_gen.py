from depends.model import generate_response
from typing import List
from unstructured.documents.elements import Element
import re

def generate_questions(elements: List[Element]) :
    context = [(element.to_dict()["type"], element.to_dict()["text"]) for element in elements]
    prompt = "You are an expert and you are formulating questions from documents to assess the knowledge of a student about content given in the json encoded document. Please formulate as many questions as possible to assess knowledge of the document given."
    system = "Give questions in pure python list of strings so that they can be converted by python list in one go using list(eval(response['response'])). Ezample response: \"['What are Bananas?', 'How Sunflowers grow?', 'How Canaries fly?']\""
    response = generate_response(prompt=prompt, system=system, context=context)
    pattern = r'\d+\.\s(.+?)\n'
    matches = re.findall(pattern, response['response'])
    return [question for question in matches]

def generate_questions_2(elements: List[Element]) :
    context = [f"\n\n{element.to_dict()['type']}:\n{element.to_dict()['text']}\page_number: {element.to_dict()['metadata']['page_number']}\nposition_in_page: {element.to_dict()['metadata']['coordinates']}" for element in elements]
    metadata = {"languages": elements[0].to_dict()['metadata']['languages'], "filetype": elements[0].to_dict()['metadata']['filetype']}
    context = f"metadata:\n{metadata}\n\njson_ended_document:\n{context}"
    prompt = "You are an expert and you are formulating questions from the document to assess the knowledge of a student about content given in the json encoded document. Please formulate as many questions as possible to assess knowledge of the document given."
    system = "You always give response in pure numbered list"
    response = generate_response(prompt=prompt, system=system, context=context)
    pattern = r'\d+\.\s(.+?)\n'
    matches = re.findall(pattern, response['response'])
    return [question for question in matches]

