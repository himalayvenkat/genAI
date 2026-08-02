from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
prompt = '''
    ### Instructions: you are a AI model that will solve code related questions only , if any questions outside the coding means say Sorry
    ### Input: write a code for factorial of n in python
    ### Response:
    '''
response = client.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[
        {
            'role':'user','content':prompt
        }
    ]
)
print(response.choices[0].message.content)