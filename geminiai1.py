# for google we need to go to "https://aistudio.google.com"

from google import genai

# here we are not giving any of the apikeys in the code , but in the terminal we need to send the code
#$env:GEMINI_API_KEY="API_KEY_VALUE_HERE"
client = genai.Client()  # this line will automatically get the key value

# or
# we can also send like this
# client = genai.Client(api_key="your_actual_api_key_here")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)