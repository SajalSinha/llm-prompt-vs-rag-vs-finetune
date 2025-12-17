# Failure Taxonomy — Prompt-Only Baseline

## 1. Structural Failures
- Output is not valid JSON
- Missing required fields
- Extra unexpected fields

## 2. Hallucination
- Field values not present in source document
- Fabricated numeric limits or conditions

## 3. Aggregation Errors
- Multiple entities merged into one
- Only last entity extracted
- Partial overwrite of fields

## 4. Omission
- Entity present in document but missing in output
- Exceptions not captured

## 5. Overgeneration
- Repeats input prompt
- Adds explanations instead of JSON
