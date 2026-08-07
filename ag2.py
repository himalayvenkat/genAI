from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

load_dotenv()

client = OpenAI()

# ----------------- Tool -----------------
def get_Temp(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

# ----------------- Tool Definition -----------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_Temp",
            "description": "Get the current weather of a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# ----------------- User Query -----------------
messages = [
    {
        "role": "user",
        "content": "What is the temperature in Hyderabad now?"
    }
]

# ----------------- First LLM Call -----------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# ----------------- Execute Tool -----------------
if message.tool_calls:

    tool_call = message.tool_calls[0]

    args = json.loads(tool_call.function.arguments)

    weather = get_Temp(args["city"])

    # Add assistant message
    messages.append(message)

    # Add tool response
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": weather
        }
    )

    # ----------------- Final LLM Call -----------------
    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    print(final_response.choices[0].message.content)

else:
    print(message.content)