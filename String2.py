text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for ch in text:
    if ch.isalpha():          
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Total characters:", len(text))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
