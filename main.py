import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():

    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('Usage: uv run main.py "prompt here"')
        print('Example: uv run main.py Can I use boot.dev to become a better programmer?')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages)
        
def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages
    )
    print("Response:")
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
