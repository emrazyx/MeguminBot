import twitter, json, requests, time, os

consumerKey = os.environ['consumer_key']
consumerSecret = os.environ['consumer_secret']
accessTokenKey = os.environ['access_token_key']
accessTokenSecret = os.environ['access_token_secret']
api = twitter.Api(consumer_key = consumerKey, consumer_secret = consumerSecret, access_token_key = accessTokenKey, access_token_secret = accessTokenSecret)
lastImageUrl = ""

def checkReddit():
	global lastImageUrl
	if lastImageUrl == "":
		api.PostUpdate("I'm running!")
	with requests.get('https://www.reddit.com/r/megumin/new.json', headers={'user-agent': 'OreganoMeguminBot'}) as url:
		meguminData = json.loads(url.content)['data']['children'][0]['data']
		meguminImage = meguminData['url']
		meguminLink = "https://reddit.com" + meguminData['permalink']
		if (meguminImage != lastImageUrl):
			api.PostMedia(meguminLink, meguminImage)
			lastImageUrl = meguminImage
			time.sleep(600) # sleep for 10 minutes
			checkReddit()

checkReddit()
