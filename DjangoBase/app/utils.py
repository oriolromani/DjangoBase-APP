

def longest_word(list_of_words, word):
    """
    Return the longest item on list_of_words containing the characters on word
    :param list_of_words: list of strings
    :param word: string
    """
    previous_result = ''
    consider = True
    for given_word in list_of_words:
        word_copy = word
        for c in given_word:
            if c not in word_copy:
                consider = False
                break
            else:
                word_copy.replace(c, '')
                consider = True
        if consider and len(given_word) > len(previous_result):
            previous_result = given_word
    return previous_result
