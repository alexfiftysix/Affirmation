from random import randint, choice

SENTENCE_STRUCTURES = [x.strip() for x in open('word_lists/sentence_structures.txt').readlines() if len(x) > 1]
BIRTHDAY_SENTENCES = [x.strip() for x in open('word_lists/birthday_sentences.txt').readlines() if len(x) > 1]
ADJECTIVES = [x.strip() for x in open('word_lists/adjectives.txt').readlines() if len(x) > 1]
QUALIFIERS = [x.strip() for x in open('word_lists/qualifiers.txt').readlines() if len(x) > 1]
NOUNS = [x.strip() for x in open('word_lists/nouns.txt').readlines() if len(x) > 1]
EMOTIONS = [x.strip() for x in open('word_lists/emotions.txt').readlines() if len(x) > 1]
NICE_THINGS = [x.strip() for x in open('word_lists/nice_things.txt').readlines() if len(x) > 1]


def contains_tag(string: str, which_tag: str) -> bool:
    return string.__contains__('{' + which_tag + '}')


def write_affirmation(sentence_structures, adjectives, qualifiers, nouns, emotions, nice_things, name="<name>",
                      sender=None):
    # TODO: Rewrite with format
    # Eg/proof. '{a}{c}'.format(a="a", b="b", c="c")

    structure = sentence_structures[randint(0, len(sentence_structures) - 1)]
    contains_adj = '{adj}' in structure
    contains_qual = '{qual}' in structure
    contains_noun = '{noun}' in structure
    contains_emotion = '{emotion}' in structure
    contains_name = '{recipient}' in structure
    contains_nice_thing = '{nice_thing}' in structure

    adjective = choice(adjectives)
    qualifier = choice(qualifiers)
    noun = choice(nouns)
    emotion = choice(emotions)
    nice_thing = choice(nice_things)

    sentence: str = structure
    if contains_qual:
        sentence = sentence.replace('{qual}', qualifier)
    if contains_adj:
        sentence = sentence.replace('{adj}', adjective)
    if contains_noun:
        sentence = sentence.replace('{noun}', noun)
    if contains_emotion:
        sentence = sentence.replace('{emotion}', emotion)

    if contains_nice_thing:
        sentence = sentence.replace('{nice_thing}', nice_thing)

    sentence += '!'
    sentence = sentence.capitalize()
    sentence = convert_a_to_an(sentence)

    if contains_name:
        sentence = sentence.replace('{recipient}', name.capitalize())
        if sender:
            sentence += f' From {sender}'

    sentence = capitalize_i(sentence)
    sentence = capitalize_first_letter_of_sentence(sentence)

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


def capitalize_first_letter_of_sentence(sentence: str) -> str:
    """
    Given a sentence, converts the first letter of each sentence to a capital
    :param sentence:
    :return:
    """
    sentence = sentence[:]

    for index in range(len(sentence)):
        if index == 0:
            sentence = sentence[0].upper() + sentence[1:]
        elif sentence[index] == '.' and len(sentence) > index + 2:
            previous = sentence[:index + 2]
            converted = sentence[index + 2].upper()
            next = sentence[index + 3:]

            sentence = previous + converted + next

    return sentence


def generate_birthday_message(birthday_person, sender=None):
    return write_affirmation(BIRTHDAY_SENTENCES, ADJECTIVES, QUALIFIERS, NOUNS, EMOTIONS, NICE_THINGS,
                             name=birthday_person, sender=sender)


def generate_affirmation():
    """
    Function for most uses - writes a positive affirmation
    Eg "You're a winner!"
    """
    return write_affirmation(SENTENCE_STRUCTURES, ADJECTIVES, QUALIFIERS, NOUNS, EMOTIONS, NICE_THINGS)
