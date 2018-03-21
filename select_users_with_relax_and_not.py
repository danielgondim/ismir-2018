import os

from distutils.dir_util import copy_tree

DIRECTORY_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/relax"
DIRECTORY_NOT_RELAX = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/not_relax/"

user_with_relax = os.listdir(DIRECTORY_RELAX)
user_with_not_relax = os.listdir(DIRECTORY_NOT_RELAX)

intersected_users = []

for user in user_with_relax:
	if user in user_with_not_relax:
		intersected_users.append(user)

for user in intersected_users:
	from_directory = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/relax/" + user
	to_directory = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/" + user
	copy_tree(from_directory, to_directory)


from_directory = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/relax/" + user
to_directory = "/home/danielgondim/workspace-new/phd/experiments/ismir-2018/8tracks/both/relax/" + user
copy_tree(from_directory, to_directory)