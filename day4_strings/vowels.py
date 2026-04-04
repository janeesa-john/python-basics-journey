#Count vowels in a word

word = input("Enter a word: ")
vowels = "AEIOUaeiou"
count_vowel = 0
for ch in word:
    if ch in vowels:
        count_vowel+=1
print("Numbers of vowels: ",count_vowel)