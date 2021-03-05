#!/usr/bin/env python3

# check version of python Im using
# import sys
# print(sys.version)

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

vowel_count = 0
consonant_count = 0

word = input("Enter your value: ")
print("Analyzing vowels and consonants in " + word)

for char in word:
	if (char in vowels):
		vowel_count += 1
	if (char in consonants):
		consonant_count += 1

print(word + " contains: \r\n" + str(vowel_count) + " vowel(s) \r\n" + str(consonant_count) + " consonant(s).")

