import re

pattern = r"[a-z]+e"
text = """Shrutika
             tayde
             is here...!!!"""

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(text[match.span()[0] : match.span()[1]])
