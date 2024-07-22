from ollama import generate
from typing import Optional, Any

def generate_response(prompt: str, system: Optional[str] = None, context: Optional[Any] = None) -> str:
    context = str(context) if context else None
    new_prompt = f"context: {context}\n\n{prompt}" if context else prompt

    return generate(model="llama3", prompt=new_prompt, system=system)
