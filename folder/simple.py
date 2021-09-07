import os

def print_dir():
	print('the items in the folder are:\n'+'\n'.join('{}: {}'.format(*k) for k in enumerate(os.listdir())))

def summa(x, y):
	return x+y

# plus comment
# extra comment
# will that be okay