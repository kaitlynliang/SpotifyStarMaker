import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid ='4ccf9617ddf84730956abb7515e65176'
secret = '7cfa7b7def4f4e7d8af0d9fccf87b12c'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

largedict=dict()

years=['2015','2016','2017','2018','2019']
for yr in years:
	print(yr)
	for i in range(0,1000,50):
	    track_results = sp.search(q='year:'+yr, type='track', limit=50,offset=i)
	    for i, t in enumerate(track_results['tracks']['items']):
	    	if t['artists'][0]['id'] not in largedict:
	    		id1=t['artists'][0]['id']
	    		largedict[id1]=[t['artists'][0]['name'],sp.artist(id1)['popularity']]

artists=[]
popularity=[]
danceability=[]
energy=[]
loudness=[]
mode=[]
speechinesss=[]
acousticness=[]
instrumentalness=[]
liveness=[]
valence=[]
tempo=[]

for key in largedict:
	audio_features={'danceability':0,'energy':0,'loudness':0,'mode':0,'speechiness':0,'acousticness':0,'instrumentalness':0,'liveness':0,'valence':0,'tempo':0}
	tracks=0
	p=0
	for track in sp.artist_top_tracks(key)['tracks']:
		if int(track['album']['release_date'][0:4])<2015 or int(track['album']['release_date'][0:4])>2019:
			continue
		a=sp.audio_features(track['id'])
		if not a[0]:
			continue
		tracks+=1
		p+=float(track['popularity'])/3
		for k in audio_features:
			audio_features[k]+=float(a[0][k])/3
		if tracks==3:
			break

	if tracks!=3:
		continue
	popularity.append(round(p,3))
	artists.append(largedict[key][0])
	danceability.append(round(audio_features['danceability'],3))
	energy.append(round(audio_features['energy'],3))
	loudness.append(round(audio_features['loudness'],3))
	mode.append(round(audio_features['mode'],3))
	speechinesss.append(round(audio_features['speechiness'],3))
	acousticness.append(round(audio_features['acousticness'],3))
	instrumentalness.append(round(audio_features['instrumentalness'],3))
	liveness.append(round(audio_features['liveness'],3))
	valence.append(round(audio_features['valence'],3))
	tempo.append(round(audio_features['tempo'],3))

track_dataframe = pd.DataFrame({'artist' : artists, 'popularity' : popularity, 'danceability' : danceability,
 'energy': energy, 'loudness': loudness, 'mode': mode,'speechiness': speechinesss, 'acousticness': acousticness,
 'instrumentalness': instrumentalness, 'liveness': liveness, 'valence': valence, 'tempo':tempo})
print(track_dataframe)
track_dataframe.head()
track_dataframe.to_csv(path_or_buf='sample.csv')

'''artists=[]
popularitys=[]
danceability=[]
energy=[]
loudness=[]
mode=[]
speechinesss=[]
acousticness=[]
instrumentalness=[]
liveness=[]
valence=[]
tempo=[]

i=0
print('!!!')
for key in largedict:
	audio_features={'danceability':0,'energy':0,'loudness':0,'mode':0,'speechiness':0,'acousticness':0,'instrumentalness':0,'liveness':0,'valence':0,'tempo':0}
	length=len(largedict[key])
	for i in largedict[key]:
		a=sp.audio_features(i[0])
		if not a[0]:
			continue
		pop=i[1]/length
		for k in audio_features:
			audio_features[k]+=float(a[0][k])/length
	if not a[0]:
		continue
	print(audio_features)
	artists.append(key)
	popularitys.append(pop)
	danceability.append(audio_features['danceability'])
	energy.append(audio_features['energy'])
	loudness.append(audio_features['loudness'])
	mode.append(audio_features['mode'])
	speechinesss.append(audio_features['speechiness'])
	acousticness.append(audio_features['acousticness'])
	instrumentalness.append(audio_features['instrumentalness'])
	liveness.append(audio_features['liveness'])
	valence.append(audio_features['valence'])
	tempo.append(audio_features['tempo'])

print('!!!')
track_dataframe = pd.DataFrame({'artist' : artists, 'popularity' : popularitys, 'danceability' : danceability,
 'energy': energy, 'loudness': loudness, 'mode': mode,'speechiness': speechinesss, 'acousticness': acousticness,
 'instrumentalness': instrumentalness, 'liveness': liveness, 'valence': valence, 'tempo':tempo})
print(track_dataframe.shape)

track_dataframe.head()

track_dataframe.to_csv(path_or_buf='sample.csv')'''



'''artist_name.append(t['artists'][0]['name'])
track_id.append(t['id'])
popularity.append(t['popularity'])'''

'''track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
print(track_dataframe.shape)
track_dataframe.head()

track_dataframe.to_csv(path_or_buf='sample.csv')'''


'''birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])'''