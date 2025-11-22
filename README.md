import json
import re

def text_to_json(text: str):
    # 1. Remove markdown code fences like ```json or ```
    cleaned = re.sub(r"```json|```", "", text).strip()
    
    # 2. Find the first { ... } JSON block
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in the text.")
    
    json_str = match.group(0)
    
    # 3. Convert to Python dict
    return json.loads(json_str)
