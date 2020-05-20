import tweepy
import bot_settings

auth = tweepy.OAuthHandler(bot_settings.consumer_key, bot_settings.consumer_secret)
auth.set_access_token(bot_settings.access_token, bot_settings.access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
print(user.name)
print(user.followers_count)
print(user.id)
print(api.show_friendship(source_id='243369006', target_screen_name='kisuly808'))
api.destroy_friendship(screen_name='kisuly808')
print(api.show_friendship(source_id='243369006', target_screen_name='kisuly808').values)