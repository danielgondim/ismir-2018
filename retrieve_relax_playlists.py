#-*- coding:utf-8 -*-
import MySQLdb, csv, os

DIRECTORY = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/relax/"

db = MySQLdb.connect(host="localhost",    
                     user="root",         
                     passwd="moti1989",  
                     db="8tracks",       
                     charset="utf8",
                     use_unicode=True)     

cur = db.cursor()

query = "SELECT M.user_id, MT.mix_id, T.name, T.performer FROM 8tracks.mixes AS M, 8tracks.mixes_tracks AS MT, 8tracks.tracks AS T WHERE (M.id = MT.mix_id AND MT.track_id = T.id AND M.tag_list_cache LIKE '%relax%');"

cur.execute(query)

playlists_count = 0

current_row = cur.fetchmany()

while current_row != ():
	current_playlist = []
	header = ['user_id','mix_id','track_name','artist_name']
	current_playlist.append(header)
	user_id = current_row[0][0]
	mix_id = current_row[0][1]
	track_name = current_row[0][2]

	if track_name == None:
		track_name = ''
	else:
		track_name = track_name.encode('utf-8')

	artist_name = current_row[0][3]
	if artist_name == None:
		artist_name = ''
	else:
		artist_name = artist_name.encode('utf-8')

	while (current_row[0][1] == mix_id):
		track_name = current_row[0][2]
		if track_name == None:
			track_name = ''
		else:
			track_name = track_name.encode('utf-8')
		
		artist_name = current_row[0][3]
		if artist_name == None:
			artist_name = ''
		else:
			artist_name = artist_name.encode('utf-8')

		current_playlist.append([user_id, mix_id, track_name, artist_name])
		current_row = cur.fetchmany()
		if (current_row == ()):
			break

	playlist_directory = "%s%s" % (DIRECTORY, user_id)

	if not os.path.exists(playlist_directory):
		os.makedirs(playlist_directory)
	
	with open("%s/%s.csv" % (playlist_directory, mix_id), 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(current_playlist)

	playlists_count += 1
	print 'Playlist %d' % playlists_count