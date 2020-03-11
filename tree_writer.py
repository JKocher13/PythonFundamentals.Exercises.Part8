import os
given path = os.getcwd()


def print_in_tree(lst):
	with open (tree.txt, w) as file:
		for x in lst:
			print x


def get_full_path(given_path)
	x = os.path.abspath(give_path)
	return x

def get_initial_list(path):
	lst = os.listdir(path)
	return lst

def get_child_directories(lst):
	for x in lst:
		lst.append(os.listdir(x))

lst = get_child_directories(get_initial_list(get_full_path(x)))

print_tree(lst)