from random import randint, choice, seed

SENTENCE_STRUCTURES = [x.strip() for x in open('word_lists/sentence_structures.txt').readlines() if len(x) > 1]
ADJECTIVES = [x.strip() for x in open('word_lists/adjectives.txt').readlines()]
QUALIFIERS = [x.strip() for x in open('word_lists/qualifiers.txt').readlines()]
NOUNS = [x.strip() for x in open('word_lists/nouns.txt').readlines()]
EMOTIONS = [x.strip() for x in open('word_lists/emotions.txt').readlines()]


def rand_from_list(list_of_stuff):
    return choice(list_of_stuff)


def contains_tag(string: str, which_tag: str) -> bool:
    return string.__contains__('{' + which_tag + '}')


def write_affirmation(sentence_structures, adjectives, qualifiers, nouns, emotions, seed_value):
    structure = sentence_structures[randint(0, len(sentence_structures) - 1)]
    contains_adj = '{adj}' in structure
    contains_qual = '{qual}' in structure
    contains_a = '{a}' in structure
    contains_noun = '{noun}' in structure
    contains_emotion = '{emotion}' in structure

    adjective = rand_from_list(adjectives)
    qualifier = rand_from_list(qualifiers)
    noun = rand_from_list(nouns)
    emotion = rand_from_list(emotions)

    sentence: str = structure
    if contains_qual:
        sentence = sentence.replace('{qual}', qualifier)
    if contains_adj:
        sentence = sentence.replace('{adj}', adjective)
    if contains_noun:
        sentence = sentence.replace('{noun}', noun)
    if contains_emotion:
        sentence = sentence.replace('{emotion}', emotion)

    sentence += '!'
    sentence = sentence.capitalize()
    sentence = convert_a_to_an(sentence)
    sentence = capitalize_i(sentence)

    return sentence


def capitalize_i(sentence: str) -> str:
    sentence = sentence[:]
    punctuation = """ "')([]{}.,!"""

    while True:
        got_to_end = True
        small_i_at = -1
        for index in range(len(sentence) - 1):
            if len(sentence) > index + 1 and sentence[index] == 'i' and (
                    index == 0 or sentence[index - 1] in punctuation) and sentence[index + 1] in punctuation:
                small_i_at = index + 1
                got_to_end = False
                break

        if got_to_end:
            break
        elif small_i_at != -1:
            start = sentence[:small_i_at - 1]
            end = sentence[small_i_at:]
            sentence = start + 'I' + end

    return sentence


def convert_a_to_an(sentence: str) -> str:
    """
    Given a sentence, converts 'a' to 'an' where required
    Eg: 'a egg' would become 'an egg'
    """
    vowels = 'aeiou'

    while True:
        got_to_end = True
        hanging_a_at = -1
        for index in range(len(sentence) - 1):
            if len(sentence) > index + 1 and sentence[index] == 'a' and (index == 0 or sentence[index - 1] == ' ') and \
                    sentence[index + 1] == ' ' and sentence[index + 2] in vowels:
                hanging_a_at = index + 1
                got_to_end = False
                break

        if got_to_end:
            break
        elif hanging_a_at != -1:
            start = sentence[:hanging_a_at]
            end = sentence[hanging_a_at:]
            sentence = start + 'n' + end

    return sentence


def generate_affirmation(seed_value):
    """
    Function for most uses - writes a positive affirmation
    Eg "You're a winner!"
    """
    return write_affirmation(SENTENCE_STRUCTURES, ADJECTIVES, QUALIFIERS, NOUNS, EMOTIONS, seed_value)
