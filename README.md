# llm-prompt-vs-rag-vs-finetune

# Prompting vs RAG vs Fine-tuning — A Controlled LLM Study

## Motivation
LLM-powered products frequently face a key architectural decision:
Should we rely on prompt engineering, retrieval-augmented generation (RAG), or fine-tuning?

This repository presents a controlled empirical study comparing these approaches
on a realistic information extraction task, focusing on accuracy, reliability,
cost, and failure modes.

## Hypothesis
1. Prompt-only approaches are fastest to deploy but brittle under distribution shift.
2. RAG improves controllability and factual grounding but introduces retrieval failure modes.
3. Fine-tuning improves task accuracy but risks overfitting and miscalibration.

## Task Definition
The task is structured information extraction from long, semi-structured documents
(e.g. policy or legal-style text).

The target output schema is:

```json
{
  "entity": "",
  "condition": "",
  "numeric_limit": "",
  "exceptions": ""
}
