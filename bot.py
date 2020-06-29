import twitter, json, requests, time, os, dropbox, random, math


api = twitter.Api(consumer_key = '4tycy2cbPBmuiot87SoUPSQZF', consumer_secret = '8U0ltWsK14F7MY1T7TvSy88h856cBP8VOHLkIgCIlyifzIaftP', access_token_key = '1120022500862234626-A488oXn3YFqkmZKQ6bMeeLL2aHDWZr', access_token_secret = 'SXSqg1IvXjRGM3xqVKcKNMLZFRLVXnfbgIVTPDTbFxyE8')
client = dropbox.Dropbox(os.environ['megumin_dropbox_key'])

def postMegumin():
	meguminFolder = client.files_list_folder('').entries
	randomIndex = math.floor(random.random() * len(meguminFolder))
	randomImage = client.sharing_create_shared_link('/' + meguminFolder[randomIndex].name).url[:-1] + '1'
	api.PostMedia('', randomImage)

while True: 
	postMegumin()
	time.sleep(3600) # sleep for 10 minutes
