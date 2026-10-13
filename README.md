# Experiment 8: Structured vs. Unstructured Output

## Aim
To demonstrate how prompt engineering can produce structured Markdown output and compare its readability with an unstructured paragraph.

## Problem Statement
Use an LLM to describe Python, Java, and C++ in two formats:
- Unstructured: A short paragraph.
- Structured: A Markdown table with specified columns.

## Technologies Used
- Python
- Google Gemini AI
- Google Gen AI SDK

## Algorithm
1. Initialize the Gemini API client.
2. Define the programming language information.
3. Create an unstructured prompt.
4. Create a structured prompt specifying the table columns and rows.
5. Send both prompts to the same model with identical parameters.
6. Print both responses.
7. Compare readability and ease of information retrieval.
8. Save the results to a text file.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration
Set the `GEMINI_API_KEY` environment variable before running the program. Never upload API keys to GitHub.

## Execution

```bash
python src/main.py
```

## Expected Output
- An unstructured paragraph describing the three languages.
- A Markdown comparison table.
- A brief readability analysis.
- Results saved in `output/comparison_results.txt`.

## Result
The experiment compares paragraph-based output with a Markdown table generated from the same source information.

## Conclusion
Unstructured text is useful for general explanations, while structured tables make it easier to compare multiple items using consistent attributes. Clear output-format instructions help the LLM organize information for readability.


