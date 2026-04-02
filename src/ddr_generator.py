import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

def generate_ddr(context):

    prompt = f"""
You are a highly experienced civil engineer and inspection analyst.

Your task is to generate a professional DDR (Detailed Defect Report).

IMPORTANT:
The input may contain OCR errors, noise, or incomplete data.

DATA:
{context}

STEP 1: Evaluate data quality:
- Good
- Partial
- Poor / Corrupted

STEP 2:
- If GOOD → full analysis
- If PARTIAL → mix of real + cautious insights
- If POOR → DO NOT guess → clearly say limitations

OUTPUT FORMAT:

### 1. Property Issue Summary

### 2. Area-wise Observations
- Confirmed findings
- Unclear / OCR noise

### 3. Probable Root Cause
(Only if supported, else "Not Available")

### 4. Severity Assessment
(Low / Medium / High / Cannot be assessed + reason)

### 5. Recommended Actions
(Always give practical steps)

### 6. Additional Notes

### 7. Missing Information

STRICT RULES:
- DO NOT hallucinate
- DO NOT assume meanings from random text
- If unsure → say "Not Available"
- Keep it professional and realistic
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a strict and reliable engineering report generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )

    return response.choices[0].message.content