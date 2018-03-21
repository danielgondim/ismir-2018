import os, shutil

'''
SOURCE_DIRECTORY = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/not_relax/"

DESTINATION_DIRECTORY = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both_sample/not_relax/"

files = os.listdir(SOURCE_DIRECTORY)

print files[2032]

files = files[1201:2033]

count = 1201

for file in files:
	print "Copying file number %d..." % count
	source = SOURCE_DIRECTORY + file
	destination = DESTINATION_DIRECTORY + file
	shutil.copytree(source, destination)
	count += 1
'''

#SCRIPT PARA PEGAR AS MESMAS PASTAS PARA O RELAX

DIRECTORY_NOT_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both_sample/not_relax/"
DIRECTORY_SOURCE_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/"
DIRECTORY_DESTINATION_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both_sample/relax/"

files_not_relax = os.listdir(DIRECTORY_NOT_RELAX)

count = 1

for file in files_not_relax:
	print "Copying file number %d..." % count
	source = DIRECTORY_SOURCE_RELAX + file
	destination = DIRECTORY_DESTINATION_RELAX + file
	shutil.copytree(source, destination)
	count += 1