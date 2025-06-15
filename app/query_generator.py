# query_generator.py
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql(question, model="gpt-3.5-turbo"):
    prompt = (
        "Convert the following natural language request to a SQL query. "
        "Return only the SQL query and nothing else.\n"
        f"Request: {question}\nSQL:"
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
        temperature=0
    )
    return response.choices[0].message.content.strip()
