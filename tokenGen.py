import tiktoken

text = "I Love You Baby"

encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(text)

print(tokens)