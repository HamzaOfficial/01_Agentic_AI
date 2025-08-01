from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.run import RunConfig
import asyncio
import os
from dotenv import load_dotenv,find_dotenv


_: bool = load_dotenv(find_dotenv())

gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")

#print("gemin_api_key ->", gemini_api_key)



# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# config = RunConfig(
#     model=llm_model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

math_agent: Agent = Agent(name="MathAgent") # gemini-2.5 as agent brain - chat completions


#"""Procedure 01"""
# result: Runner = Runner.run_sync(math_agent, "10 /2")
# print("\nCALLING AGENT\n")
# print(result.final_output)

#"""Procedure 02"""
async def call_agent():
    config = RunConfig(
    model=llm_model,
    model_provider=external_client,
    tracing_disabled=True
    )
    output = await Runner.run(starting_agent=math_agent,
                              input= "10 /2",
                              run_config=config)
    print(output.final_output)

asyncio.run(call_agent())