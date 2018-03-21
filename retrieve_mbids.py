#-*- coding:utf-8 -*-
#!/usr/bin/python
import musicbrainz, acousticbrainz, glob, os, csv

def retrieve_mbid_and_tags(song_name, artist_name):
	MBIDs = musicbrainz.retrieveMBID(song_name, artist_name)
	if len(MBIDs) > 0:
		for id in MBIDs:
			acoustic_tags = acousticbrainz.retrieveHighLevelFeatures(id)
			if acoustic_tags != {}:
				data_to_return = {}
				for tag in acoustic_tags['highlevel']:
					if tag.startswith('mood') or tag.startswith('genre'):
						data_to_return[tag] = {}
						for sub_tag in acoustic_tags['highlevel'][tag]:
							if not sub_tag.startswith('ve'):
								data_to_return[tag][sub_tag] = acoustic_tags['highlevel'][tag][sub_tag]
				return data_to_return
	return {}

files = os.listdir("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/")

for file in files[5917:]:
	folder = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/" + file + "/*.csv"
	archives = glob.glob(folder)
	print "User %s has %d playlists" % (file, len(archives))

	count = 1

	for archive in archives:
		print "Trying to retrieve informations from the playlist number %d from this user" % count
		new_content = []
		with open(archive, 'rb') as playlist_input:
			reader = csv.reader(playlist_input)
			header = reader.next()
			if len(header) < 5:
				print "Retrieving informations..."
				header.append('mbids')
				new_content.append(header)
				for row in reader:
					track_name = row[2]
					artist_name = row[3]
					mbids = musicbrainz.retrieveMBID(track_name, artist_name)
					row.append(mbids)
					new_content.append(row)
	
				with open("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/" + file + "/" + archive.split("/")[-1], 'w') as output:
					writer = csv.writer(output, lineterminator='\n')
					writer.writerows(new_content)
			else:
				print "User already accounted"

		count += 1

'''
count = 0
for file in files:
	count += 1
	new_content = []
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		for column in NEW_COLUMNS:
			header.append(column + '_value')
			header.append(column + '_prob')
		new_content.append(header)
		for row in reader:
			if row[8] == 'TRUE':
				data = retrieve_ab_data(row[7])
				for information in data:
					row.append(information)
			new_content.append(row)
	
	with open(NEW_DIRECTORY + file, 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(new_content)
	print count
'''