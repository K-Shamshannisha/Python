s="Hello, World!"
def count_vowel_and_const(s):
    vowels='aeiou'
    s=s.lower()
    vowel_count=0
    consonant_count=0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count,consonant_count
vowels,consonants=count_vowel_and_const(s)
print(f"Vowels:{vowels},Consonants:{consonants}")