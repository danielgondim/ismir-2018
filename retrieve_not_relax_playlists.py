#-*- coding:utf-8 -*-
import MySQLdb, csv, os

DIRECTORY_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/relax"
DIRECTORY_NOT_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/not_relax/"

db = MySQLdb.connect(host="localhost",    
                     user="root",         
                     passwd="moti1989",  
                     db="8tracks",       
                     charset="utf8",
                     use_unicode=True)     

cur = db.cursor()

user_with_relax = os.listdir(DIRECTORY_RELAX)

user_with_not_relax = os.listdir(DIRECTORY_NOT_RELAX)

user_count = 0

for user in user_with_relax:

	if user not in user_with_not_relax:
		print "O usuario %s nao esta em not_relax e vai ter seus dados consultados no banco." % (user)
		query = "SELECT M.user_id, MT.mix_id, T.name, T.performer FROM 8tracks.mixes AS M, 8tracks.mixes_tracks AS MT, 8tracks.tracks AS T WHERE (M.user_id = " + user + " AND M.id = MT.mix_id AND MT.track_id = T.id AND M.tag_list_cache NOT LIKE '%relax%');"
		cur.execute(query)

		playlists_count = 0
		user_count += 1

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

			playlist_directory = "%s%s" % (DIRECTORY_NOT_RELAX, user_id)

			if not os.path.exists(playlist_directory):
				os.makedirs(playlist_directory)
		
			with open("%s/%s.csv" % (playlist_directory, mix_id), 'w') as output:
				writer = csv.writer(output, lineterminator='\n')
				writer.writerows(current_playlist)

			playlists_count += 1
			print 'Playlist %d for the user number %d' % (playlists_count, user_count)
	else:
		print "O usuario %s ja possui not_relax e suas informacoes nao serao consultadas no banco" % (user)

	user_with_not_relax = os.listdir(DIRECTORY_NOT_RELAX)