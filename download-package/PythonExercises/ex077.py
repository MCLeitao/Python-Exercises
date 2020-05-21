# Create a program that has a tuple with several words (do not use accents).
# After that, you must show, for each word, what are your vowels.

words = ('lear', 'program', 'language', 'python',
         'course', 'free', 'study', 'practice',
         'work', 'market', 'programmer', 'future')
for word in words:
    print(f'\nIn the word {word.upper()} we have', end=' ')
    for letter in word:  # Each word is a list
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
