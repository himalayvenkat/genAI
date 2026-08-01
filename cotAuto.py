# from openai import OpenAI
# import json
# from dotenv import load_dotenv
# load_dotenv()
# client = OpenAI()
# response = client.chat.completions.create(
#     model='gpt-4.1-mini',
#     messages=[
#         {
#             'role':'system',
#             'content':'''You will solve only the maths & code related queries and answers them , you will
#             solve or give the answer in three process 1.START 2.PLAN 3.OUTPUT
            
#             start means user input and see what he is asking
#             plan means you have to think the approach to solve the problem in many ways and take the best and most efficient way to solve that
#             output means you need to give the answer
            
#             Rules:
#             - Strictly follow the output format
#             - execute one step only in a run
            
#             Output Format:
            
#             {{
#                 'Step':'Start'|'Plan'|'Output'|None
#                 'content':'string'
#             }}
            
#             Examples:
            
#             {
#                 'Step':'Start',
#                 'content':'user is asking to solve 2*3+10-7+1000/5'
#             }
#             {
#                 'Step':'Plan',
#                 'content':'solving 2*3+10-7+200'
#             }
#             {
#                 'Step':'Plan',
#                 'content':'solving 6+10-7+200'
#             }
#             {
#                 'Step':'Output',
#                 'content':'209'
#             }
#             {
#                 'Step':'Output',
#                 'content':'Sorry i can not answer this one, ask me questions related to code & Maths'
#             }
#             '''
#         },
#         {
#             'role':'user',
#             'content':'2*3+10-7+200 '
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({'Step':'Start','content':'user is asking to solve the expression 2*3+10-7+200'})
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({"Step": "Plan", "content": "First calculate multiplication 2*3=6, then add 10, subtract 7, and add 200 stepwise for accurate result"})
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({"Step": "Plan", "content": "solving 6+10-7+200"})
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({"Step": "Plan", "content": "solving 16-7+200"})
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({"Step": "Plan", "content": "solving 9+200"})
#         }

#     ]
# )
# print(response.choices[0].message.content)



############ the Above one is manual , but now the below code will automate it

from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()
client = OpenAI()
assistant_array = [
            {
                'role':'system',
                'content':'''You will solve only the maths & code related queries and answers them , you will
                solve or give the answer in three process 1.START 2.PLAN 3.OUTPUT
                
                start means user input and see what he is asking
                plan means you have to think the approach to solve the problem in many ways and take the best and most efficient way to solve that
                output means you need to give the answer
                
                Rules:
                - Strictly follow the output format
                - execute one step only in a run
                
                Output Format:
                
                {{
                    "Step":"Start"|"Plan"|"Output"|None
                    "content":"string"
                }}
                
                Examples:
                
                {
                    "Step":"Start",
                    "content":"user is asking to solve 2*3+10-7+1000/5"
                }
                {
                    "Step":"Plan",
                    "content":"solving 2*3+10-7+200"
                }
                {
                    "Step":"Plan",
                    "content":"solving 6+10-7+200"
                }
                {
                    "Step":"Plan",
                    "content":"209"
                }
                {
                    'Step':'Output',
                    'content':'Sorry i can not answer this one, ask me questions related to code & Maths"
                }
                '''
            },
            {
                'role':'user',
                'content':'2*3+10-7+200 '
            }
        ]
isLoop = True
while isLoop:
    response = client.chat.completions.create(
        model='gpt-4.1-mini',
        messages= assistant_array
    )
    jsonObject = json.loads(response.choices[0].message.content)

    print(jsonObject)

    if jsonObject['Step'] == "Start" or jsonObject['Step'] == "Plan":
            obj = {
                'role':'assistant',
                'content':response.choices[0].message.content
            }
            assistant_array.append(obj)
            continue
    else: 
            print(response.choices[0].message.content)
            isLoop = False
            break
  
    
############ loads -----> will make a string into dict
################ dumps ----> will make a object into string