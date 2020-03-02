import tweepy
import time  
import bot_settings

auth = tweepy.OAuthHandler(bot_settings.consumer_key, bot_settings.consumer_secret)
auth.set_access_token(bot_settings.access_token, bot_settings.access_token_secret)

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

for followers in tweepy.Cursor(api.followers).items():
    print(followers.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)





# print(user.name)
# print(user.screen_name)
# print(dir(user))
# print(user.status)
# print(user.followers_count)
# print(user.id)
#===Unfollow from friend use id
# print(api.show_friendship(source_id='243369006', target_screen_name='kisuly808'))
# api.destroy_friendship(screen_name='kisuly808')
# print(api.show_friendship(source_id='243369006', target_screen_name='kisuly808')['following'])