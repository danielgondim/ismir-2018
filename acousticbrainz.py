import requests

moods_list = ['mood_electronic', 'mood_party', 'mood_aggressive', 'mood_acoustic', 'mood_happy', 'mood_sad', 'mood_relaxed']

def mood_translator(value):
	if value.startswith("not_"):
		return 0
	return 1

def retrieveHighLevelFeatures(mbid):
	try:
		response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/high-level?n=0')
		data = response.json()
		if len(data) <= 1:
			return {}
		return data
	except:
		return {}

def retrieveLowLevelFeatures(mbid):
	try:
		response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/low-level?n=0')
		data = response.json()
		if len(data) <= 1:
			return {}
		return data
	except:
		return {}