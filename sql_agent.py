import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def load_schema():

    with open(
        "database_schema.md",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()



def generate_sql(question):

    schema = load_schema()

    prompt = f"""
You are an expert PostgreSQL developer.

Convert the user's natural language question into a SQL query.

Database schema:

{schema}


User question:

{question}


Rules:
- Return only SQL.
- No explanation.
- No markdown.
- Use PostgreSQL syntax.
"""


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You generate accurate PostgreSQL SQL queries."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )


    return response.choices[0].message.content



if __name__ == "__main__":

    question = input(
        "Ask a database question: "
    )


    sql = generate_sql(question)


    print("\nGenerated SQL:")
    print("----------------")
    print(sql)