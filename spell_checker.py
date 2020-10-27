import nltk
from modules import modules

with open('database.txt', 'r') as file:
    database = file.read()


def split_word(token_list):

    """  This function returns the split of all words from what is not alpha.
    e.g., numbers, special punctuation characters, arithmetic signs, etc. """

    words_list = []
    token_words = nltk.tokenize.word_tokenize(token_list)

    for word in token_words:
        if word.isalpha():
            words_list.append(word.lower())

    return words_list


db_split_by_word = split_word(database)
vocabulary = set(db_split_by_word)

freq = nltk.FreqDist(db_split_by_word)
total = len(db_split_by_word)


def potential_word(generated_word):
    return freq[generated_word] / total


def spell_checker(word):
    generated_words = modules.word_generator(word)
    correct_word = max(generated_words, key=potential_word)

    return correct_word


def validate(words, args):

    """ This function returns the accuracy of how many words
              the model is able to get right. """

    words_count = len(words)
    count = 0
    unknown = 0

    for correct, wrong in words:
        corrected_word = spell_checker(wrong)
        unknown += correct not in vocabulary

        if corrected_word == correct:
            count += 1

    accuracy = count * 100 / words_count
    unknown_words = unknown * 100 / words_count

    print(f'Accuracy: {accuracy:.2f}% of {words_count} words.'
          f' Unknown Words are {unknown_words:.2f}%')


words_test_list = modules.create_words_test('words.txt')


