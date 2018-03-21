#-*- coding:utf-8 -*-
#!/usr/bin/python
import musicbrainz, acousticbrainz, glob, os, csv

files = os.listdir("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/")

#print files.index('192678')
#print files[4838]


count_users = 1

for file in files[4839:]:
	folder = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/" + file + "/*.csv"
	archives = glob.glob(folder)
	print "User %s has %d playlists" % (file, len(archives))
	print "It's the %d user analyzed" % (count_users)

	for archive in archives:
		if os.path.getsize(archive) == 0:
			with open("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/empty-files.txt", 'a') as empty_output:
						empty_output.write("User: %d. File: %s\n" % (file, archive))
						empty_output.close()
		else:
			print "Trying to retrieve informations from the playlist %s from this user" % archive
			new_content = []
			with open(archive, 'rb') as playlist_input:
				reader = csv.reader(playlist_input)
				header = reader.next()
				if len(header) < 5:
					header.append('mbids')
					new_content.append(header)
					for row in reader:
						track_name = row[2]
						artist_name = row[3]
						mbids = musicbrainz.retrieveMBID(track_name, artist_name)
						row.append(mbids)
						new_content.append(row)
		
					with open("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/" + file + "/" + archive.split("/")[-1], 'w') as output:
						writer = csv.writer(output, lineterminator='\n')
						writer.writerows(new_content)
	count_users += 1

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