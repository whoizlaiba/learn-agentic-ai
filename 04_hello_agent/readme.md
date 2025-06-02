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
