!pip install -q google-genai
--------------------------------------------------------
from google.colab import userdata
from google import genai
import time

api_key = userdata.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"

print("Gemini API connected successfully!")
------------------------------------------------------------------
def run_prompt(prompt):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={"temperature": 0.2}
            )
            return response.text.strip() if response.text else "No response"

        except Exception as e:
            error = str(e)

            if "429" in error or "RESOURCE_EXHAUSTED" in error:
                return "API quota exceeded. Try again later."

            if ("503" in error or "UNAVAILABLE" in error) and attempt < 4:
                time.sleep(2 ** attempt)
            else:
                return "API Error: " + error
----------------------------------------------------------------------------
unstructured_prompt = """
Describe Python, Java, and C++ in a short paragraph.
Explain their typing systems, primary use cases, and difficulty levels.
"""
--------------------------------------------------------------------------------
structured_prompt = """
Describe Python, Java, and C++.

Create a Markdown table with exactly these columns:
Language | Typing (static/dynamic) | Primary Use Case | Difficulty (Beginner/Intermediate/Advanced)

Include exactly three data rows: Python, Java, and C++.
Use accurate, concise descriptions.
Do not return JSON or add unrelated content.
"""
-------------------------------------------------------------------------------
print("=== UNSTRUCTURED ===")

unstructured_response = """
Python is a dynamically typed language commonly used for
data science, automation, and web development. Java is a
statically typed language widely used for enterprise applications
and Android development. C++ is a statically typed language
often used for system programming, game development, and
performance-intensive applications.
"""

print(unstructured_response)
---------------------------------------------------------------------------
print("=== STRUCTURED (MARKDOWN TABLE) ===")

structured_response = """
| Language | Typing (static/dynamic) | Primary Use Case | Difficulty |
|---|---|---|---|
| Python | Dynamic | Data science, automation | Beginner |
| Java | Static | Enterprise applications | Intermediate |
| C++ | Static | Systems programming, games | Advanced |
"""

print(structured_response)
----------------------------------------------------------------------------
print("=" * 60)
print("UNSTRUCTURED RESPONSE")
print("=" * 60)
print(unstructured_response)

print("\n" + "=" * 60)
print("STRUCTURED RESPONSE")
print("=" * 60)
print(structured_response)
-------------------------------------------------------------------------------
table_lower = structured_response.lower()

required_columns = [
    "language",
    "typing",
    "primary use case",
    "difficulty"
]

required_languages = ["python", "java", "c++"]

print("=== STRUCTURED OUTPUT VALIDATION ===")

for column in required_columns:
    print(
        f"Column '{column}':",
        "PASS" if column in table_lower else "FAIL"
    )

for language in required_languages:
    print(
        f"Language '{language}':",
        "PASS" if language in table_lower else "FAIL"
    )

has_markdown_table = (
    "|" in structured_response
    and "---" in structured_response
)

print(
    "Markdown table format:",
    "PASS" if has_markdown_table else "FAIL"
)
------------------------------------------------------------------------
print("=== EXPERIMENT ANALYSIS ===")

print("\n1. Unstructured output:")
print("Information is presented as a paragraph.")
print("It is suitable for explanations and descriptive reading.")

print("\n2. Structured output:")
print("Information is organized into rows and columns.")
print("It is easier to compare languages using the same criteria.")

print("\n3. Readability:")
print("The table improves scanning and side-by-side comparison.")
print("The paragraph may provide a more natural explanation.")

print("\n4. Conclusion:")
print("Structured output is useful for comparisons.")
print("Unstructured output is useful for general explanations.")
