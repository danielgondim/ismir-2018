#-*- coding:utf-8 -*-
#!/usr/bin/python
import musicbrainz, acousticbrainz, glob, os, csv, requests, json

files = os.listdir("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/")

#ja recuperei até o índice 2032!!

files = files[2033:3453]

count_user = 1067

for file in files:
	folder = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/"	 + file + "/*.csv"
	archives = glob.glob(folder)
	print "User %s (number %d) has %d playlists" % (file, count_user, len(archives))

	count = 1

	for archive in archives:
		print "Trying to retrieve low-level features from the playlist %s from this user" % archive.split('/')[-1]
		new_content = []
		with open(archive, 'rb') as playlist_input:
			reader = csv.reader(playlist_input)
			header = reader.next()
			if len(header) < 6:
				header.append('low_level')
				new_content.append(header)
				for row in reader:
					mbid = row[4]
					if mbid != '[]':
						mbid = mbid[3:-2]
						print "Retrieving features..."
						response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/low-level?n=0')
						print mbid
						data = response.json()
						if len(data) > 1:
							path = '/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/' + file + '/' + mbid + '.json'
							with open(path, 'w') as f:
								json.dump(data, f)
							row.append(path)
					new_content.append(row)
	
				with open("/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/" + file + "/" + archive.split("/")[-1], 'w') as output:
					writer = csv.writer(output, lineterminator='\n')
					writer.writerows(new_content)
		count += 1
	count_user += 1