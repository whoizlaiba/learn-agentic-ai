# **_LiteLLM Python SDK_**

**Watch:** *LiteLLM - One Unified API for all LLMs*  
**Repo** | **Docs** | **Colab**

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
