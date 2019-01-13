from TwitterSearch import TwitterSearchOrder, TwitterSearchException, TwitterSearch
from .config import CONFIG
import logging
from .models import Politician

def getTweets(politician_id):
	try:

		politician = Politician.objects.get(id=politician_id)

		politician_names = [politician.first_name + " " + politician.last_name, politician.last_name, politician.username]
		print("Getting Tweets for " + str(politician.first_name + " " + politician.last_name))
		tso = TwitterSearchOrder()			
		sexistWords = CONFIG["SEXISTWORDS"]
		searchTerms = []

		for word in sexistWords:
			for politician in politician_names:
				searchTerms.append(word + ' ' + politician)
		
		tso.set_keywords(searchTerms, or_operator=True)
		print(searchTerms)
		tso.set_language("en")
		tso.set_include_entities(False)
		querystr = tso.create_search_url()
		tso.set_search_url(querystr + "&tweet_mode=extended")

		ts = TwitterSearch(
            consumer_key = CONFIG["CONSUMER_KEY"],
            consumer_secret = CONFIG["CONSUMER_SECRET"],
            access_token = CONFIG["ACCESS_TOKEN"],
            access_token_secret = CONFIG["ACCESS_TOKEN_SECRET"]
        )
		
		return ts.search_tweets_iterable(tso)

	except TwitterSearchException as e:
		logging.exception("Unable to get new tweets because of"  + str(e))

# if __name__ == "__main__":
#     getTweets()