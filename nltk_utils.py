import nltk
from nltk.stem.porter import PorterStemmer
# Download if you get any error.
# nltk.download('punkt')
stemmer = PorterStemmer()


# To split the sentence into a list of words
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


# This is where a word will be stemmed.
def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass