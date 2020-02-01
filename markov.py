import pickle
import re
import spacy

def normalize(text):
    text = re.sub(r'#.+', '', text)
    text = re.sub(r'https?://.+', '', text)
    text = re.sub(r'@\w+', '', text)

    return text.strip()

def tokenize(file_path):
    nlp = spacy.load('ja_ginza')

    words = []
    beginnings = []
    endings = []

    with open(file_path) as f:
        lines = f.readlines()

    for line in lines:
        text = normalize(line)

        if not text:
            continue

        doc = nlp(text)

        for sent in doc.sents:
            if len(sent) < 3:
                continue

            sent_words = [token.orth_ for token in sent]

            words.extend(sent_words)
            beginnings.append(tuple(sent_words[:2]))
            endings.append(tuple(sent_words[-2:]))

    return words, beginnings, endings

def make_markov(words):
    markov = {}
    w1, w2, *words = words

    for word in words:
        if (w1, w2) not in markov:
            markov[(w1, w2)] = []

        markov[(w1, w2)].append(word)
        w1, w2 = w2, word

    return markov

def main():
    print('Tokenizing...')

    words, beginnings, endings = tokenize('tweets.txt')

    print('Finished!')

    data = {
        'markov': make_markov(words),
        'beginnings': beginnings,
        'endings': endings,
    }


    with open('markov.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
