# 🤖 OpenAI Agents using Google Gemini Models

This guide demonstrates how to use the **OpenAI Agents SDK** with **Google Gemini models** by leveraging OpenAI-compatible endpoints provided by Google. You'll learn how to set up and configure Gemini as your LLM provider at various levels: **Agent**, **Run**, and **Global**.

---

## 🔗 Key Resources

- 📘 OpenAI Agents Docs: [openai-agents-python](https://openai.github.io/openai-agents-python/)
- 📄 Gemini with OpenAI API Docs: [Google AI Gemini API](https://ai.google.dev/gemini-api/docs/openai)
- 🔧 Supported Models: [OpenAI Agents Models](https://openai.github.io/openai-agents-python/models/)

---

## ⚙️ Setup Instructions

1. **Create a `.env` file** with your Google Gemini API Key:

    ```
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

2. **Initialize project using `uv`**:

    ```bash
    uv init hello_agent
    cd hello_agent
    uv add openai-agents python-dotenv
    ```

3. **Run your agent**:

    ```bash
    uv run main.py
    ```

---

## 🧠 How to Configure Gemini as LLM Provider

The OpenAI Agents SDK defaults to OpenAI models, but you can override it to use **Google Gemini** via the OpenAI-compatible API at various levels:

---

### 🧪 1. Agent-Level Configuration

```python
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

result = await Runner.run(agent, "Tell me about recursion in programming.")
print(result.final_output)
