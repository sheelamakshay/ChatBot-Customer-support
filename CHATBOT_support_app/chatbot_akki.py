import openai
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key securely from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to handle conversation and generate responses from OpenAI's model
def CustomChatGPT(user_input, messages):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Gradio interface setup
def gradio_interface():
    # Ask the user for the type of chatbot they want to create
    system_msg = input("What type of chatbot would you like to create?\n")
    messages = [{"role": "system", "content": system_msg}]

    print("Your new assistant is ready!")

    # Function to handle user input and generate chatbot responses
    def interface(user_input):
        return CustomChatGPT(user_input, messages)

    # Create Gradio interface
    demo = gr.Interface(fn=interface, inputs="text", outputs="text", title="Custom Chatbot")
    demo.launch(share=True)

# Function to generate app ideas with OpenAI's API
def generate_app_ideas():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
    print(completion.choices[0]["message"]["content"])

# Main function to control the flow of the program
if __name__ == "__main__":
    # Ask the user if they want to use the chatbot interface or generate app ideas
    choice = input("Do you want to use the chatbot interface? (y/n): ")
    
    if choice.lower() == 'y':
        # Launch Gradio interface
        gradio_interface()
    else:
        # Generate 3 app ideas with OpenAI's API
        print("Generating app ideas using OpenAI API...")
        generate_app_ideas()
