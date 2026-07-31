from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
question = input("Hi i am Chat GPT , What you want to know ? ")
response = client.chat.completions.create(
    model="gpt-4.1-mini-2025-04-14",
    messages=[
        {
            "role":"system","content":"you will solve/explain only maths related questions and answers,if they are asking any other questions say sorry"
        },
        {
            "role":"user","content":question
        }
    ]
)

print(response.choices[0].message.content)

# Output 1
# Hi i am Chat GPT , What you want to know ? explain about pythogorus threom
# The Pythagorean Theorem is a fundamental principle in geometry that relates the lengths of the sides of a right-angled triangle. It states:

# In a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

# Mathematically, if the sides are labeled as:
# - \(a\) and \(b\) for the legs (the two sides that form the right angle)
# - \(c\) for the hypotenuse

# then the theorem is expressed as:
# \[
# c^2 = a^2 + b^2
# \]

# This theorem allows you to find the length of one side if the lengths of the other two sides are known.

# For example, if one leg \(a = 3\) units and the other leg \(b = 4\) units, then the hypotenuse \(c\) is:
# \[
# c = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
# \]

# So, the hypotenuse is 5 units long.


# Output 2
# Hi i am Chat GPT , What you want to know ? how is the temperature today in Hyderabad
# Sorry, I can only help with math-related questions.

