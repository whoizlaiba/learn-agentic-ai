# LiteLLM Agent SDK with Google Gemini

This repository provides a Jupyter Notebook (`03_Litellm_agent_sdk.ipynb`) that demonstrates how to use the `openai-agents` SDK with LiteLLM to integrate Google Gemini models for building conversational agents.

## 🛠️ Prerequisites

- Python 3.6+
- Jupyter Notebook or JupyterLab
- (Optional) Google Colab for cloud execution
- A valid Google Gemini API key

## 📦 Installation

Install required packages:

```python
!pip install -Uq openai-agents "openai-agents[litellm]" 
```
Enable async support:


```python
import nest_asyncio
nest_asyncio.apply()
```
Set up your Gemini API key (in Google Colab):


```python
from google.colab import userdata
GEMINI_API_KEY = userdata.get("GEMINI_API_KEY")
```
##  📓 Notebook Overview
The notebook includes the following steps:

1. Install SDK: Installs openai-agents and LiteLLM integration.

2. Enable Async Support: Uses nest_asyncio for compatibility.

3. Create Conversational Agent:

- Uses LiteLLM with the Google Gemini model.

- Defines a function tool (get_weather) to simulate weather retrieval.

- Configures the agent to respond only in haikus.

- Runs the agent synchronously using Runner.run_sync.

## 🧠 Key Code Example

```python
from agents import Agent, Runner, function_tool
from agents.extensions.models.litellm_model import LitellmModel

MODEL = 'gemini/gemini-2.0-flash'

@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
)

result = Runner.run_sync(agent, "What's the weather in Tokyo?")
print(result.final_output)
```
## 💬 Sample Output

```arduino
Skies now partly clear,  
Seventy degrees in Tokyo,  
Gentle breeze abounds.
```
## 🚀 Usage Instructions
1. Open the notebook 03_Litellm_agent_sdk.ipynb in Jupyter or Colab.

2. Set your Gemini API key.

3. Run the cells step-by-step.

4. Modify the model or query as desired.

## ⚠️ Notes
- get_weather is a placeholder—replace it with real weather API calls for production.

- Tracing is disabled (set_tracing_disabled(True)) to keep output clean—enable it for debugging.

- Always store your API key securely (avoid hardcoding).
