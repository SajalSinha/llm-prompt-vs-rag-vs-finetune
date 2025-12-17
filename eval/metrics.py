# def is_valid_json(output: str) -> bool:
#     pass

def field_accuracy(predicted: dict, gold: dict) -> float:
    pass

def hallucination_rate(predicted: dict, source_text: str) -> float:
    pass

import json

def is_valid_json(output: str) -> bool:
    try:
        json.loads(output)
        return True
    except Exception:
        return False

