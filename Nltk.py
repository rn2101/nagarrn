import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello  david, what's up? The season is great, and the game is awesome. . You shouldn't eat unhealthy."

print(word_tokenize(example_text))
