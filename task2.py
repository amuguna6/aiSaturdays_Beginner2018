import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhrase
ReverseWord = randomPhrase[::-1]
$ cd aiSaturdays_Beginner2018
$ git pull origin master
print (ReverseWord)
