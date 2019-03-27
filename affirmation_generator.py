from random import randint

SENTENCE_STRUCTURES = [x.strip() for x in open('word_lists/sentence_structures.txt').readlines() if len(x) > 1]
ADJECTIVES = [x.strip() for x in open('word_lists/adjectives.txt').readlines()]
QUALIFIERS = [x.strip() for x in open('word_lists/qualifiers.txt').readlines()]
NOUNS = [x.strip() for x in open('word_lists/nouns.txt').readlines()]
EMOTIONS = [x.strip() for x in open('word_lists/emotions.txt').readlines()]


def rand_from_list(list_of_stuff):
    # TODO: This must be in the rand library, just use the lib function
    return list_of_stuff[randint(0, len(list_of_stuff) - 1)]


def contains_tag(string: str, which_tag: str) -> bool:
    return string.__contains__('{' + which_tag + '}')


def write_affirmation(sentence_structures, adjectives, qualifiers, nouns, emotions):
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
    # TODO: support a/an before adjectives or qualifiers

    # print("Structure: {}\nAdjective: {}\nQual: {}\nA/An: {}\nNoun: {}\nEmotion: {}\n---".format(
    #     structure, adjective, qualifier, a_an, noun, emotion
    # ))

    sentence: str = structure
    if contains_a:
        sentence = sentence.replace('{a}', a_an)
    if contains_qual:
        sentence = sentence.replace('{qual}', qualifier)
    if contains_adj:
        sentence = sentence.replace('{adj}', adjective)
    if contains_noun:
        sentence = sentence.replace('{noun}', noun)
    if contains_emotion:
        sentence = sentence.replace('{emotion}', emotion)

    punctuation = ' .,!'
    sentence += '!'
    sentence = convert_a_to_an(sentence)

    for x in punctuation:
        for y in punctuation:
            sentence.replace('{}i{}'.format(x, y), '{}I{}'.format(x, y))

    return sentence.capitalize()


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


def generate_affirmation():
    """
    Function for most uses - writes a positive affirmation
    Eg "You're a winner!"
    """
    return write_affirmation(SENTENCE_STRUCTURES, ADJECTIVES, QUALIFIERS, NOUNS, EMOTIONS)


print(generate_affirmation())
