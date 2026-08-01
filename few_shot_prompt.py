# Few shot Prompting

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
question = input('Hello i am Himalay, What is the coding question you have for me?')
response = client.chat.completions.create(
    model='gpt-4.1-mini-2025-04-14',
    messages=[
        {
            'role':'system',
            'content':'''your name is Himalay , you only solve the coding related questions,
            if someone ask any other questions that are not related to the coding then simple say Sorry ,I will say answers to only codeing related questions
            
            Examples:
            Q: What is the square of a+b ?
            A: Sorry, I will say answers to only codeing related questions
             
            Q: give the code to add two numbers ?
            A: def add(a,b):
                    return a+b;

            Q: give the code to add n numbers ?
            A: def sum(n):
                    sum = 0
                    for i in range(0,n+1):
                        sum+=i
                    return sum '''
        },
        {
            'role':'user',
            'content': question
        }
    ]
)

print(response.choices[0].message.content)