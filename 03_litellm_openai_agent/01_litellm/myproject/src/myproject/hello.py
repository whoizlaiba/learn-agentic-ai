from litellm import completion  # type: ignore
import os

os.environ["OPENAI_API_KEY"] = "your_openai_key_here"
os.environ["GEMINI_API_KEY"] = "your_gemini_key_here"

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{"content": "What's the capital of France?", "role": "user"}]
    )
    print(response.choices[0].message.content)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Tell me a fun fact about space.", "role": "user"}]
    )
    print(response.choices[0].message.content)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"content": "Who wrote 'To Kill a Mockingbird'?", "role": "user"}]
    )
    print(response.choices[0].message.content)

# Optional: call one of them to test
if __name__ == "__main__":
    gemini()  # Change to openai() or gemini2() to test others
