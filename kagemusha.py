import random
from janome.tokenizer import Tokenizer

def generate_sentence(markov, head_word_pairs):
    sentence = ''
    (w1, w2) = random.choice(head_word_pairs)

    sentence += w1 + w2

    while True:
        if (w1, w2) not in markov:
            return sentence

        word = random.choice(markov[(w1, w2)])

        if word == '\n' or word == '。':
            return sentence

        sentence += word

        w1, w2 = w2, word

def make_markov(all_words):
    markov = {}
    w1, w2, *all_words = all_words

    for word in all_words:
        if (w1, w2) not in markov:
            markov[(w1, w2)] = []

        markov[(w1, w2)].append(word)
        w1, w2 = w2, word

    return markov

def main():
    with open('./tweets.txt') as f:
        lines = f.readlines()

    all_words = []
    head_word_pairs = []
    t = Tokenizer()

    for line in lines:
        words = t.tokenize(line + '。', wakati = True)

        if len(words) < 3:
            continue

        all_words.extend(words)
        head_word_pairs.append((words[0], words[1]))

    markov = make_markov(all_words)

    sentences = []
    for i in range(0, 5):
        sentence = generate_sentence(markov, head_word_pairs)
        sentences.append(sentence)

    print(max(sentences, key = lambda x: len(x)))

if __name__ == '__main__':
    main()
