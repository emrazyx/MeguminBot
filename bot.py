import twitter, json, requests, time

consumerKey = 'XBwg9fDh0ACXzZb3yYiYxv1nu'
consumerSecret = '9VtSPiTutZPDCntndFOtttYRvzWcAxSsdhWJznbllOxMI2prYn'
accessTokenKey = '2972389871-3yQQBePK9X7opd3cshn7fgOpCCQMMkVUtvDmdhs'
accessTokenSecret = 'wzSgHwo23S3yj2DwGSyOoeEyYrwXt37zJV8A94r4Fm9gS'
api = twitter.Api(consumer_key = consumerKey, consumer_secret = consumerSecret, access_token_key = accessTokenKey, access_token_secret = accessTokenSecret)
lastImageUrl = ""

def checkReddit():
	if lastImageUrl == "":
		api.PostUpdate("I'm running!")
	with requests.get('https://www.reddit.com/r/megumin/new.json', headers={'user-agent': 'OreganoMeguminBot'}) as url:
		meguminData = json.loads(url.content)['data']['children'][0]['data']
		meguminImage = meguminData['url']
		meguminLink = "https://reddit.com" + meguminData['permalink']
		if (meguminImage != lastImageUrl):
			api.PostMedia(meguminLink, meguminImage)
			lastImageUrl = meguminImage
			time.sleep(3600)
			checkReddit()

checkReddit()
