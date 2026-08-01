# chain of thoughts  is a process where , the model will think and gives the best model as the output

# Few shot Prompting
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
# question = input('Hello i am Himalay, What is the coding question you have for me?')
response = client.chat.completions.create(
    model='gpt-4.1-mini-2025-04-14',
    messages=[
        {
            'role':'system',
            'content':'''your name is Himalay , you only solve the coding related questions and also maths questions,
            if someone ask any other questions that are not related to the coding then simple say Sorry ,I will say answers to only codeing related questions
            you need to implemet these steps before givivng the result START(User input),PLAN(Needs to think how can we solve the Problem/question),OUTPUT(Gives the final result)
            
            Rules:
            - Strictly follow Json Format in the output
            - Always Plan in different ways and take the best approch
            - there can be so many plans also
            - while planing mention it in each step also
            - Always Say in which paln you are opting and why also 

            - ONLY RUN ONE STEP AT A TIME

            Output Format:
            {{
                'step':"Start"|'Plan'|'Output'|'None',
                'content':'string'
            }}

            Examples:
            Q: How is the weather in safilguda ?
            A: {
                'step': 'None',
                'content': 'Sorry, I will say answers to only codeing related questions'
            }
             
            Q: solve this 2*3+10/5
            A: {
                'step': 'Start',
                'content': 'seems like user has give a maths problem'
            }
            

            '''
        },
        {
            'role':'user',
            'content': "factorial of n numbers"
        },
        # Manually writing the steps
        {
            
            'role':'assistant',
            'content': json.dumps({
                                    "step": "Start",
                                    "content": "User wants to find the factorial of a number n."
                                })
        },
        {
            'role':'assistant',
            'content': json.dumps({"step": "Plan", "content": "Plan 1: Use a recursive function to compute the factorial, which is simple and elegant but may cause stack overflow for large n. Plan 2: Use an iterative approach with a loop, which is efficient and safe for large numbers. Plan 3: Use Python's built-in math.factorial function for simplicity and performance. Opting for Plan 2 (iterative) as it balances efficiency and safety without relying on built-in functions."})
        }

    ]
)

print(response.choices[0].message.content)


# - ONLY RUN ONE STEP AT A TIME

# THIS WILL MAKES THE SYSTEM TO STOP AFTER ONE STEP , OTHERWISE IT WILL EXECUTE ALL THE STEPS AND GIVES OUTPUT
# FOR THE NEXT STEP WE NEED TO WRITE THE CODE MANUALLY

# # Outputs

# {
#     "step": "Start",
#     "content": "seems like user has given a maths problem to solve"
# }
# {
#     "step": "Plan",
#     "content": "First, follow the order of operations: multiplication and division from left to right, then addition and subtraction. Calculate 5*10=50, 35/5=7, then the expression becomes 50 + 7 - 10. Finally, compute 50 + 7 = 57 and 57 - 10 = 47"
# }
# {
#     "step": "Output",
#     "content": "The result of the expression 5*10+35/5-10 is 47"
# }



# Output for n numbers

# {
#   "step": "Start",
#   "content": "User wants a code to add n numbers."
# }
# {
#   "step": "Plan",
#   "content": "Plan 1: Use a loop to take n numbers as input and keep adding to a sum variable. This is straightforward and efficient.\nPlan 2: Use the built-in sum() function on a list of n numbers taken as input, which is concise and pythonic.\nPlan 3: Use recursion to add n numbers, but this can be less efficient and complex for beginners.\nI will go with Plan 2 because it is concise, efficient, and easy to understand."
# }
# {
#   "step": "Output",
#   "content": "def add_n_numbers():\n    n = int(input('Enter how many numbers you want to add: '))\n    numbers = list(map(int, input(f'Enter {n} numbers separated by space: ').split()))\n    if len(numbers) != n:\n        print('Number of inputs does not match n')\n        return\n    total = sum(numbers)\n    print('Sum of numbers is:', total)\n\n# Call the function\nadd_n_numbers()"
# }