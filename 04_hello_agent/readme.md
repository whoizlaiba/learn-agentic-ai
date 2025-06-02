# **_Google Gemini with OpenAI Agents SDK_**

**_Quickstart to use Google Gemini models with the OpenAI Agents Python SDK._**

---

### **_Setup and Run Commands_**

1. Create a `.env` file in your project root with your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
Initialize your project and install dependencies:

bash
Copy
Edit
uv init hello_agent
cd hello_agent
uv add openai-agents python-dotenv
uv run main.py
How to Configure Google Gemini as LLM Provider
The OpenAI Agents SDK defaults to OpenAI models, but you can configure Google Gemini models at three levels: Agent, Run, and Global.

1. Agent Level Configuration
Set the Gemini client directly when creating an Agent instance:

python
Copy
Edit
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "your_api_key_here"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )
    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
2. Run Level Configuration
Use a RunConfig to specify the Gemini client and model during a run:

python
Copy
Edit
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "your_api_key_here"

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)
print(result.final_output)
3. Global Level Configuration
Set Gemini client globally for all agents and runs:

python
Copy
Edit
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

gemini_api_key = "your_api_key_here"

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Hello")
print(result.final_output)
Useful Links
OpenAI Agents SDK Documentation

OpenAI Agents Supported Models

Google Gemini API Docs

yaml
Copy
Edit

---

This block has everything — instructions, code snippets, commands, and links — all formatted and ready for GitHub markdown. Just paste it in!




