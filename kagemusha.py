import pickle
import random

def generate_sentence(markov, beginnings, endings):
    sentence = ''

    (w1, w2) = random.choice(beginnings)
    sentence += w1 + w2

    while True:
        if (w1, w2) not in markov:
            return sentence

        if (w1, w2) in endings:
            return sentence

        word = random.choice(markov[(w1, w2)])
        sentence += word

        w1, w2 = w2, word

def main():
    with open('markov.pickle', 'rb') as f:
        data = pickle.load(f)

    markov = data['markov']
    beginnings = data['beginnings']
    endings = data['endings']

    sentences = [generate_sentence(markov, beginnings, endings) for _ in range(0, 5)]
    best_sentence = max(sentences, key = lambda x: len(x))

    print(best_sentence)

if __name__ == '__main__':
    main()
