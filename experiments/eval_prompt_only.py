import json
from experiments.prompt_only import extract
from eval.metrics import is_valid_json

with open("data/processed/gold.json") as f:
    dataset = json.load(f)

results = []

for sample in dataset:
    output = extract(sample["document"])
    valid = is_valid_json(output)

    results.append({
        "document": sample["document"],
        "valid_json": valid,
        "raw_output": output
    })

for r in results:
    print("VALID JSON:", r["valid_json"])
    print(r["raw_output"])
    print("-" * 40)
