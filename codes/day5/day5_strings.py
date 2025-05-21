# Strings Manipulation : split, join, replace and strip

import re

# split()

sentence = "Python is fun"
words = sentence.split()
print(words)

# join()
new_sentence = "|".join(words)
print(new_sentence)


text = "I love Python"
updated_text = text.replace("Python", "JavaScript")
print(updated_text)

messy = "     Hello, World     "
print(messy)
cleaned_text = messy.strip()
print(cleaned_text)