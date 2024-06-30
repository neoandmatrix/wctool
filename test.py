import re

text = "hello my name is \n and trying this"

print(text)
result = re.findall(r'\w+ \n',text)
print(result)
