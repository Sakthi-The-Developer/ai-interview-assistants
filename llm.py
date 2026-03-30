import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def ask_llm(question):
    prompt = f"""
    You are an expert interview assistant.

    Give a clear, professional, short answer.

    Question: {question}
    """

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text