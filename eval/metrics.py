# def is_valid_json(output: str) -> bool:
#     pass

def field_accuracy(predicted: dict, gold: dict) -> float:
    pass

def hallucination_rate(predicted: dict, source_text: str) -> float:
    pass

# import json

# def is_valid_json(output: str) -> bool:
#     try:
#         json.loads(output)
#         return True
#     except Exception:
#         return False

import json
import re

def extract_json_block(output: str) -> str | None:
    match = re.search(r"<json>(.*?)</json>", output, re.DOTALL)
    if not match:
        return None
    return match.group(1).strip()

def is_valid_json(output: str) -> bool:
    try:
        extracted = extract_json_block(output)
        if extracted is None:
            return False
        json.loads(extracted)
        return True
    except Exception:
        return False


