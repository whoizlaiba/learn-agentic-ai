import os
from dotenv import load_dotenv  # type: ignore
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel  # type: ignore
from agents.run import RunConfig  # type: ignore
import asyncio

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    agent = Agent(
        name="Quizzy Agent",
        instructions="""
You are Quizzy, a fun and clever riddle and quiz-solving assistant. When a user provides a riddle, analyze it carefully, break it down logically, and respond with:
1. A brief explanation of how you solved it.
2. The final answer in bold.

Keep your tone friendly and smart. If the riddle is unclear, ask for clarification.
""",
        model=model
    )

    # Example riddle prompt
    user_riddle = "I can fill a room but take up no space. What am I?"

    result = await Runner.run(agent, user_riddle, run_config=config)
    print("\nCALLING QUIZZY AGENT\n")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())