from openai import OpenAI
from dotenv import load_dotenv
question = input("What you want to know?")
load_dotenv()
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4.1-mini",messages=[
        {
            "role":"user",
            "content":question
        }
    ]
)
print(response.choices[0].message.content)
print("*********************************")
print(response)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(response.choices)
print('*****************************************')
print(response.choices[0].message)




# output

#  An LLM is a large language model, an AI that processes and generates human-like text based on vast data.
#  *********************************

# ChatCompletion(id='chatcmpl-E7P1LLHPJQO2JsjVhjCnZtShVGsXD', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='An LLM is a large language model, an AI that processes and generates human-like text based on vast data.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1785433183, model='gpt-4.1-mini-2025-04-14', object='chat.completion', moderation=None, service_tier='default', system_fingerprint='fp_fdaf0aa920', usage=CompletionUsage(completion_tokens=23, prompt_tokens=19, total_tokens=42, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=None, cached_tokens=0)))
#    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# [Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='An LLM is a large language model, an AI that processes and generates human-like text based on vast data.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))]
# *****************************************
# ChatCompletionMessage(content='An LLM is a large language model, an AI that processes and generates human-like text based on vast data.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None)