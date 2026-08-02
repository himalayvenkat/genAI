from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
prompt = '''
[INST] what is the use of AI [/INST]
'''
response = client.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[
        {
            'role':'user',
            'content': prompt
        }
    ]
)
print(response.choices[0].message.content)




####### INST + SYSTEM 

prompt = '''
[INST] 
<<SYS>> you will only answer only code and AI related quries. If not say Sorry <</SYS>>

expalin 5+10+15 [/INST]
'''
response = client.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[
        {
            'role':'user',
            'content': prompt
        }
    ]
)
print(response.choices[0].message.content)