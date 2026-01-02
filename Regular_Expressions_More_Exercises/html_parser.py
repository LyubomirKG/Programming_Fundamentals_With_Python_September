import re

html = input()

# Extract title
title_match = re.search(r"<title>(.*?)</title>", html)
title = title_match.group(1) if title_match else ""

# Extract body content
body_match = re.search(r"<body>(.*?)</body>", html, re.DOTALL)
body_content = body_match.group(1) if body_match else ""

# Remove all HTML tags: anything between < and >
content = re.sub(r"<.*?>", "", body_content)

# Replace escaped newline tags "\n" with space
content = content.replace("\\n", " ")

# Normalize whitespace
content = " ".join(content.split())

print(f"Title: {title}")
print(f"Content: {content}")
