from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

load_dotenv()
client = OpenAI()

# tool
def getTemp(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response_weather = requests.get(url)
    return response_weather.text

# tool def
tools = [
    {
        "type":"function",
        "function":{
            "name":"getTemp",
            "description":"used to get the temp",
            "parameters":{
                "type": "object",
                "properties":{
                    "city":{
                        "type":"string"
                    }
                },
                "required":["city"]
            }
        }
    }
]

# user Query
messages = [
    {
        "role":"user",
        "content":"What is the temp in safilguda "
    }
]
# First LLM call
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

resp = response.choices[0].message
messages.append(resp)
# print(resp)
if resp.tool_calls:
    # args = json.loads(resp.tool_calls[0].function.arguments)
    t1 = resp.tool_calls[0]
    args = json.loads(t1.function.arguments)
    weather_Response = getTemp(args["city"])
    # message append
    messages_tool = {
        "role":"tool",
        "tool_call_id":t1.id,
        "content":weather_Response
    }
    messages.append(messages_tool)

    # Final LLm call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    print(response.choices[0].message.content)


else:
    print(resp.content)