from openai import OpenAI
from dotenv import load_dotenv
import requests

def get_Temp(city):

    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

systemPrompt = '''
    Rules:
    - you are an agent Named Monsoon , you will tell only the weather data, that to you will say the real time data
    - you will strictly adaher to rules
    - First extarct the City for which we want the temperature (Example : Delhi,Hyderabad...)
    - Call the method get_temp with the city param
    - give that response as the output

    Output Format:
                {{
                    'step':"Start"|'Plan'|'Output'|Tool|'None',
                    'content':'string'
                }}

    Examples:
    Q: What is the temperature of Delhi?

    Step1: city = Delhi
    Step2: calling the method get_Temp(city)
    A: Partly Cloudy  +27°C

    Tools:
    - get_Temp(city)
    
    
'''

load_dotenv()
def main():
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content": systemPrompt
            },
            {
                "role":"user",
                "content":"What is the temperature in hyderabad now"
            }
        ]
    )
    
    print(response.choices[0].message.content)
main()