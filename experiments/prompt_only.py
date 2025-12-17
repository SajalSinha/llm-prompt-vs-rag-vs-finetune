from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

#MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
MODEL_NAME = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300
)

def extract(document: str) -> str:
    prompt = open("prompts/extraction.txt").read().replace(
        "{{document}}", document
    )

    output = generator(prompt)
    return output[0]["generated_text"]

if __name__ == "__main__":
    sample_doc = """
    The policy applies to Entity A under condition X.
    The maximum allowable limit is 10 units.
    Exceptions include emergency scenarios.
    """

    print(extract(sample_doc))
