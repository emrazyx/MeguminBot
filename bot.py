import twitter, json, requests, time, os, dropbox, random, math

consumerKey = os.environ['consumer_key']
consumerSecret = os.environ['consumer_secret']
accessTokenKey = os.environ['access_token_key']
accessTokenSecret = os.environ['access_token_secret']
api = twitter.Api(consumer_key = consumerKey, consumer_secret = consumerSecret, access_token_key = accessTokenKey, access_token_secret = accessTokenSecret)
client = dropbox.Dropbox(os.environ['megumin_dropbox_key'])

def postMegumin():
	meguminFolder = client.files_list_folder('').entries
	randomIndex = math.floor(random.random() * len(meguminFolder))
	randomImage = client.sharing_create_shared_link('/' + meguminFolder[randomIndex].name).url[:-1] + '1'
	api.PostMedia('', randomImage)

while True: 
	postMegumin()
	time.sleep(3600) # sleep for 10 minutes
