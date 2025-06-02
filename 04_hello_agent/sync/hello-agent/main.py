# Import required modules
from dotenv import load_dotenv  # type: ignore # Loads environment variables from a .env file
import os  # Provides access to operating system functionality like environment variables
from agents import Agent, AsyncOpenAI, Runner, OpenAIChatCompletionsModel, RunConfig  # type: ignore # Agent-related classes

# Load environment variables from the .env file into the environment
load_dotenv()

api_key_gemini = os.getenv("GEMINI_API_KEY")



# Check if the API key is present; if not, raise an error
if not api_key_gemini:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=api_key_gemini,
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
     

agent = Agent(
    name="FinanceCalc Agent",
    instructions="You are a reliable and precise assistant designed to perform financial and mathematical calculations accurately. Assist users by computing values, solving equations, and providing clear, concise results."
    , model=model
)

response_of_agent=Runner.run_sync(
agent,
input="Calculate the total cost of 15 items each priced at $19.99 including a 7.5% sales tax.",
run_config=config
)


# Assuming the response is a RunResult object with `final_output`
clean_output = response_of_agent.final_output if hasattr(response_of_agent, 'final_output') else str(response_of_agent)

print("\nCALLING AGENT\n")
print(clean_output.strip())

