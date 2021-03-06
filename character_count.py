#!/usr/bin/env python3

sentence = ''
character = ''

def count_characters(sentence, character):
  return sentence.count(character)

sentence = input("Enter your sentence: ")
character = input("Enter the letter you would like to count: ")

count = count_characters(sentence, character)

print("Letter count: " + str(count))
