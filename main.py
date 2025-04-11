import google.generativeai as genai
import os
import sys
import argparse
import time

# Define the Gemini model ID as a constant
DEFAULT_GEMINI_MODEL_ID = "gemini-2.0-flash-thinking-exp-01-21"
model = None
chat = None

def setup_gemini_api():
    """Set up the Gemini API with the provided API key."""
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GOOGLE Gemini API Key.")
    else:
        genai.configure(api_key=api_key)

def generate_content(prompt):
    """Generate content based on the given prompt using Gemini API."""
    global chat
    try:
        setup_gemini_api()
        response = chat.send_message(prompt)
        for char in response.text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        #print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to run the Gemini chatbot."""
    global model, chat

    parser = argparse.ArgumentParser(description="Gemini Chatbot with Model Selection")
    parser.add_argument("model_name", nargs='?', default=DEFAULT_GEMINI_MODEL_ID, help="Specify the Gemini model name")
    args = parser.parse_args()

    model = genai.GenerativeModel(args.model_name)
    chat = model.start_chat(history=[])

    welcoming_text = f"""
        Welcome to Gemini Text Generator made by (Awan),
        Happy chat and talk with your Gemini Ai Generative
        (Addhe Warman Putra - Awan)

        Using model: {args.model_name}
        type 'exit()' to exit from program
    """
    print(welcoming_text)

    # while loop to keep asking user input till quitting the program   
    while True:
        prompt = input("\n> ")
        if prompt == "exit()":
            sys.exit()
        generate_content(prompt)

if __name__ == "__main__":
    main()
