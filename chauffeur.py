import function_map as ft
import time
import sys

def func_map():

	if len(sys.argv) >= 2:
		theScript = sys.argv[1]
	else:
		theScript = 'script.spy'

	file = open(theScript,'r')

	for i in file:
		desc = [x.strip() for x in i.split(',')]
		if desc[0] in ft.funcs:
			caller = ft.funcs.get(desc[0])
			if desc[0] == 'back' or desc[0] == 'forward':
				caller()
				continue
			del desc[0]
			try:
				if isinstance(float(desc[0]), float):
					desc[0] = float(desc[0])
					caller(desc[0])
			except:
				caller(desc)
	print 'done'


if __name__ == '__main__':
	func_map()


