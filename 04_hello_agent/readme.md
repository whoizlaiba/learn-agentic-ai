# **_Google Gemini with OpenAI Agents SDK_**

**_Quickstart to use Google Gemini models with the OpenAI Agents Python SDK._**

---

### **_Setup and Run Commands_**

1. Create a `.env` file in your project root with your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```
### **_Initialize and install dependencies:_**

```bash
uv init hello_agent
cd hello_agent
uv add openai-agents python-dotenv
uv run main.py
```
# **_Configuring LLM Providers Other Than OpenAI_**

**_The SDK uses OpenAI as the default, but you can configure Google Gemini at three levels:._**

---

### **_1. Agent Level_**

Set the Gemini client directly when creating an Agent instance:

```env
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

```
