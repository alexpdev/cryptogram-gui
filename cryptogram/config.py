# import os
# import sys

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# words: file containing 10,000 most commonly used words in the english language
# the words are used to help decypher the encrypted string
# words_file = os.path.join(BASE_DIR,"_words","words.pickle")


# Phrase: string encrypted the program will attempt to decrypt.
# phrase = None #'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
# optionaly you can choose to comment out phrase field above if you
# prefer and uncomment and  the phrase_path field below
# phrase_path = os.path.join(BASE_DIR,"_words","phrases.json")

# key: dictionary for {old_char:new_char} to keep track of progress.(optional)
# key = None #{"I":"X"}

# verbosity (0-3) determines the amount of information printed to stdout.
# Defaults to 1 which prints the results at certain milestones
# Levels 2 and 3 are only reccommended for debugging
# verbosity = 1

# output: optionally specify a file to store final results
# output = sys.stdout

# configuration = {
#     "BASE_DIR":BASE_DIR,
#     "words_file":words_file,
#     "key":key,
#     "phrase":phrase,
#     "phrase_path":phrase_path,
#     "verbosity":verbosity,
#     "output":output,
# }
