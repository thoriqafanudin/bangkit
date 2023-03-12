import re
result = re.search(r"[a-zA-Z]{5}", "a ghost")
print(result)

result = re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")
print(result)

result = re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")
print(result)

result = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")
print(result)

print(re.findall(r"\w{5,10}", "I really like strawberry"))

print(re.findall(r"s\w{,20}", "I really like strawberry"))