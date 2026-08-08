from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

load_dotenv()
client = OpenAI()

# Tool
def getTemp(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

# Tool Definition:
tools_def = [
    {
        "type": "function",
        "function": {
            "name":"getTemp",
            "parameters":{
                "type": "object",
                "properties":{
                    "city":{
                    "type": "string",
                    "description":"it will gives the temperature of the location"
                    }
                },
                "required":["city"]
            }
        }
    }
]

# User Query
messages = [
    {
        "role": "user",
        "content":"What is the temperature in the Hyderabad now"
    }
]

# First LLM Call:
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools_def,
    tool_choice="auto"
)
message = response.choices[0].message
# Tool Execute
if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    weather_response = getTemp(args["city"])
    # adding assistant message
    messages.append(message)
    # Add tool response
    tool_response = {
        "role":"tool",
        "tool_call_id": tool_call.id,
        "content": weather_response
    }
    messages.append(tool_response)
    print(messages)
    finalResponse = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    print(finalResponse.choices[0].message.content)
else:
    print(message.content)


