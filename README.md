# kagemusha

Generate a tweet on your behalf

## Installation

```bash
$ git clone https://github.com/dqn/kagemusha.git
$ cd kagemusha
$ pip install -r requirements.txt
```

## Usage

```bash
$ cp config.yml.sample config.yml
$ vi config.yml
# Edit config
```

```bash
$ python crawl.py # Crawl tweets
# => tweets.txt
$ python markov.py # Make markov
# => markov.pickle
$ python kagemusha.py # Generate tweet
```

## License

MIT
