# **_LiteLLM Python SDK_**

**Watch:** *[LiteLLM - One Unified API for all LLMs](https://www.youtube.com/watch?v=29_ipKNI8I0)*  
**[Repo](https://github.com/BerriAI/litellm)** | **[Docs](https://docs.litellm.ai/docs/#litellm-python-sdk)**| **[Colab](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb#scrollTo=speIkoX_8db4)**

---

**_CrewAI has transitioned to using LiteLLM_** for integrating with various Large Language Models (LLMs). **_LiteLLM serves as an intermediary_**, allowing CrewAI to connect seamlessly with multiple LLM providers. This approach offers **_flexibility in choosing the appropriate model for specific use cases_**.

Despite this shift, **_CrewAI maintains compatibility with LangChain tools_**. You can continue to integrate LangChain’s comprehensive set of tools into your CrewAI agents to enhance their capabilities.

**_In summary_**, while CrewAI now utilizes LiteLLM for LLM integrations, it still supports the use of LangChain tools within its framework.

---

## **_What is LiteLLM?_**

**_LiteLLM is a Python SDK_** designed to simplify interactions with over **_100 Large Language Models_** (LLMs) from various providers, including:

- OpenAI  
- Anthropic  
- VertexAI  
- HuggingFace  
- Azure OpenAI  
- Ollama  
- OpenRouter  

It offers:

- A **_unified interface_**
- **_Consistent output formatting_**
- Built-in **_retry and fallback mechanisms_**

---

## **_Getting Started with LiteLLM_**

### **1. Installation**

Ensure you have Python installed, then install LiteLLM:

```bash
pip install litellm
```

### **2. Setting Up Environment Variables:**

To authenticate with different LLM providers, set your API keys as environment variables. For example:

```bash
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_api_key"
# Add other keys as needed
```

### **3. Making a Completion Request:**

With LiteLLM, you can make completion requests to various models using a consistent interface. Here’s how to interact with OpenAI’s GPT-3.5-Turbo:

```bash
from litellm import completion
messages = [{"role": "user", "content": "Hello, how are you?"}]
response = completion(model="gpt-3.5-turbo", messages=messages)
print(response['choices'][0]['message']['content'])
```



For other providers, such as Anthropic’s Claude or VertexAI’s Gemini, simply change the model parameter accordingly:
### **For Anthropic's Claude**

```bash
response = completion(model="claude-2", messages=messages)
```

### *For VertexAI's Gemini*
```
response = completion(model="gemini-2.0", messages=messages)```


