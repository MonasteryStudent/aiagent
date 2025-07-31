import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from prompts import system_prompt
from call_function import available_functions

def main():

    load_dotenv()
    verbose = "--verbose" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('Usage: uv run main.py "Prompt here."')
        print('Example: uv run main.py Can I use boot.dev to become a better programmer?')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)
        
def generate_content(client, messages, verbose):


    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Response: \n{response.text}")

if __name__ == "__main__":
    main()
