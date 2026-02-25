text = input("Enter a sentence: ")
print("\nOriginal text:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalized:", text.capitalize())
print("Title case:", text.title())
print("Number of characters:", len(text))
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)
new_text = text.replace("a", "@")
print("After replacing 'a' with '@':", new_text)
print("Starts with 'Hello'? :", text.startswith("Hello"))
print("Ends with '.' ? :", text.endswith("."))
