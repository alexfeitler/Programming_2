import random

word_bank = ["TIGER", "SEAL", "MONKEY"]

my_word = word_bank.pop(random.randrange(len(word_bank)))
print(my_word)