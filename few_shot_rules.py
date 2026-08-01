# few shot prompting with structued output

from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()
client = OpenAI()
response = client.chat.completions.create(
    model='gpt-4.1-mini-2025-04-14',
    messages=[
        {
            'role':'system',
            'content':'''Answer only coding related questions, If they ask any other question say sorry i answer only questions related to coding
            
            Rules:
            - Strictly follow the JSON format for output
            
            Output Format:

            {{
                'code':"String" or None,
                'isCodingQuestion':boolean
            }}

            Examples:
            Q: What is the square of a+b ?
            A: {{
                'code':'Sorry, I will say answers to only codeing related questions',
                'isCodingQuestion': False
            }}

            Q: give the code to add two numbers ?
            A: {{
                'code': 'def add(a,b):
                            return a+b',
                'isCodingQuestion': True}}
            '''
        },
        {
            'role':'user',
            'content':'give the code to add two numbers '
        }
    ]
)

# the below line will print only the normal output the give in the output format
print(response.choices[0].message.content)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# the below line will print only the Value in the code
x = json.loads(response.choices[0].message.content)
print(x['code'])