import tweepy
import yaml

def main():
    with open('config.yml') as f:
        config = yaml.safe_load(f.read())

    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)

    texts = []
    screen_name = config['target_user_screen_name']
    max_id = None

    while True:
        statuses = api.user_timeline(
            screen_name=screen_name,
            max_id=max_id,
            tweet_mode='extended',
        )

        if not statuses:
            break

        for status in statuses:
            print(status.full_text)
            texts.append(status.full_text)

        max_id = statuses[-1].id - 1

    with open('tweets.txt', mode='w') as f:
        f.write('\n'.join(texts))

if __name__ == '__main__':
    main()
