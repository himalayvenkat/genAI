from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
askQuestion = True
while askQuestion:
    client = OpenAI(api_key="API_KEY_Value_Here",base_url="Value")
    PROMT = input("which weather info you want to know ? ")
    response=client.chat.completions.create(
        model='gemini-3.6-flash',
        messages=[
            {
                "role":"system",
                "content":"Say only Weather related queries, If they ask anything apart from that say Sorry our model works only on the Weather info only"
            },
            {
                "role":"user",
                'content':PROMT
            }
        ]
    )
    print(response.choices[0].message.content)

    x = input("Do you want to know the weather report on anything ? (Y/N)").upper()
    if(x == "Y"):
        askQuestion = True
    else:
        print("Thanks for Talking to me , Bye Hope you will have a good Day")
        askQuestion = False


# output 1:

# which weather info you want to know ? weather in safilguda now
# Currently, in Safilguda, Hyderabad, the weather is around 28°C (82°F) with partly cloudy skies. The humidity is approximately 65% with a light breeze.

# which weather info you want to know ? tirumala weather
# Tirumala generally experiences pleasant weather due to its elevation. 

# * **Average Temperature:** Ranges from 15°C to 28°C in winters, and 22°C to 35°C in summers.
# * **Best Time to Visit:** September to February, when the weather is cool and pleasant.
# * **Monsoon:** Receives rainfall from July to September.

# Would you like to know the general weather for a specific month or season?
# Do you want to know the weather report on anything ? (Y/N)y
# which weather info you want to know ? hyderabad weather
# The current weather in Hyderabad is typically warm with temperatures around 30°C (86°F), partly cloudy skies, and moderate humidity. 

# If you need a specific forecast (like daily, weekly, or rainfall updates), please let me know!
# Do you want to know the weather report on anything ? (Y/N)N
# Thanks for Talking to me , Bye Hope you will have a good Day                                                             