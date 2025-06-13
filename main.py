import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

agent: Agent = Agent(name="Website developer", instructions="Your are a helpful developer", model=model)

result =  Runner.run_sync(agent, input="How are you? i am also a developer", run_config=config)

print("Calling")
print(result.final_output)


## developer: Ali Shahid