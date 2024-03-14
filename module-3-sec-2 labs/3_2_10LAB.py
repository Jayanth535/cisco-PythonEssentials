# Prompt the user to enter a word
# and assign it to the user_word variable.
word=input("Enter the word: ")
user_word=word.upper()
vowels =['A','E','I','O','U']
res=" "
for letter in user_word:
    if letter not in vowels:
        res+=letter
for i in res:
    print(i, end='\n')
    # Complete the body of the for loop.

# output:1
#     Sample input:Gregory
# Expected output:
# G
# R
# G
# R
# Y
# Output 2
# Sample input:abstemious
# Expected output:
# B
# S
# T
# M
# S