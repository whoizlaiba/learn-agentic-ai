import os
from dotenv import load_dotenv  # type: ignore
import chainlit as cl  # type: ignore
from litellm import completion  # type: ignore
import json

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Define a system prompt to instruct the model it is a medical consultant
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a knowledgeable and empathetic medical consultant. "
        "Provide clear, accurate, and professional medical advice. "
        "Always encourage users to consult a qualified healthcare professional "
        "for serious issues. Avoid giving direct diagnoses but provide helpful guidance."
    )
}

@cl.on_chat_start
async def start():
    # Initialize chat history with the system prompt
    cl.user_session.set("chat_history", [SYSTEM_PROMPT])

    await cl.Message(content="Welcome to the Medical AI Consultant! How can I assist you with your health questions today?").send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )

        response_content = response.choices[0].message.content

        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")

@cl.on_chat_end
async def on_chat_end():
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")
