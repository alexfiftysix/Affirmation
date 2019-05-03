import nltk

# https://spacy.io - Better Natural Language processing library
# TODO: implement this
def process_sentence(original: str) -> str:
    text = nltk.word_tokenize(original)
    result = nltk.pos_tag(text)

    print(result)
    processed = original
    for x in result:
        if x[1] == 'JJ':
            # print(x)
            # print(f'<{x[0]}>')
            processed = processed.replace(x[0], '{adj}')
        if x[1] == 'NN':
            processed = processed.replace(x[0], '{noun}')
    return processed


original = 'You are a real winner.'
print(process_sentence(original))
