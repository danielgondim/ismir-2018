#-*- coding:utf-8 -*-

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    
                     user="root",         
                     passwd="moti1989",  
                     db="8tracks",       
                     charset="utf8",
                     use_unicode=True)     

cur = db.cursor()

query_relax = "SELECT user_id, COUNT(id) FROM 8tracks.mixes WHERE tag_list_cache LIKE '%relax%' GROUP BY user_id;"

cur.execute(query_relax)

current_row = cur.fetchmany()

playlists_data = {}

while current_row != ():
	user = current_row[0][0]
	if current_row[0][0] not in playlists_data:
		playlists_data[user] = current_row[0][1]
	current_row = cur.fetchmany()

query_not_relax = "SELECT user_id, COUNT(id) FROM 8tracks.mixes WHERE tag_list_cache NOT LIKE '%relax%' GROUP BY user_id;"

cur.execute(query_not_relax)

current_row = cur.fetchmany()

final_data = {}

while current_row != ():
	user = current_row[0][0]
	if current_row[0][0] in playlists_data:
		final_data[user] = {'relax':playlists_data[user], 'not_relax':current_row[0][1]}
	current_row = cur.fetchmany()

print len(final_data)

dist_users = {}

for data in final_data:
	relax = final_data[data]['relax']
	not_relax = final_data[data]['not_relax']
	string_output = 'R%d_NR%d' % (relax, not_relax)
	if string_output not in dist_users:
		dist_users[string_output] = 1
	else:
		dist_users[string_output] += 1

for qnt in range(1,51):
	current_qnt = 0
	for i in dist_users:
		relax = int(i.split('_')[0][1:])
		not_relax = int(i.split('_')[1][2:])
		if relax >= qnt and not_relax >= qnt:
			current_qnt += dist_users[i]
	print '%d usuario(s) tem pelo menos %d playlist(s) relax e %d playlist(s) não relax' % (current_qnt, qnt, qnt)