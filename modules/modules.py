
def insert_letter(slices):
    """ This function returns a new word with the letter entered. """

    new_word = []
    letters = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

    for left, right in slices:
        for letter in letters:
            new_word.append(left + letter + right)

    return new_word


def delete_characters(slices):
    """ This function delete a unwanted character and
            returns a new word list. """

    new_word = []

    for left, right in slices:
        new_word.append(left + right[1:])

    return new_word


def swap_letters(slices):
    """ This function verifies if there is a letter placed in the wrong place
     and swap this letter. e.g. compu[tr]e -> compu[te]r"""

    new_word = []
    letters = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

    for left, right in slices:
        for letter in letters:
            new_word.append(left + letter + right[1:])

    return new_word


def word_generator(word):
    """ This function returns all possible word combinations,
          separated by a letter to be entered. """

    slices = []

    for i in range(len(word) + 1):
        slices.append((word[:i], word[i:]))
    generated_word = insert_letter(slices)
    generated_word += delete_characters(slices)
    generated_word += swap_letters(slices)
    generated_word += reversing_letters(slices)

    return generated_word


def reversing_letters(slices):
    new_word = []

    for left, right in slices:
        if len(right) > 1:
            new_word.append(left + right[1] + right[0] + right[2:])

    return new_word


def reinforced_word_generator(generated_word):
    """ This function verifies whether the user has entered an extra letter
                and return a new word  """

    new_word = []

    for word in generated_word:
        new_word += word_generator(word)

    return new_word


def create_words_test(test):
    """ This function prepares the database
           to the validate function """

    words_test_list = []
    f = open('words.txt', 'r')

    for line in f:
        correct, wrong = line.split()
        words_test_list.append((correct, wrong))
    f.close()

    return words_test_list
