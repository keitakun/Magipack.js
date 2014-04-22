#!/usr/bin/env python

import os, sys, getopt
import re
import json

def listFiles(path):
	if not path.endswith('/'): path += '/'
	files = os.listdir(path)
	arr = []
	for f in files:
		if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
			arr.append([path + f, f])
		if os.path.isdir(path + '/' + f):
			arr.extend(listFiles(path + f + '/'))
	return arr

def packImages(files, dest):

	output = None
	data = []
	p = 0
	c = 0
	for fn in files:
		f = open(fn[0], 'r').read()
		l = len(f)
		if output == None: output = f
		else: output = output + f
		data.append([fn[1], p, p + l, fn[1][-3:]])
		p += l
		c += 1

	open(dest + 'images.pack', 'w').write(output)
	open(dest + 'images.json', 'w').write(json.dumps(data))

def main():
	path = dest = "."

	try:
		myopts, args = getopt.getopt(sys.argv[1:],"p:o:")
	except getopt.GetoptError as e:
		print (str(e))
		print("Usage: %s -p <path> -o <output>" % sys.argv[0])
		sys.exit(2)
	 
	for o, a in myopts:
		if o == '-p':
			path = a
		elif o == '-o':
			dest = a

	if len(path) > 0 and path[-1] != '/': path = path + '/'
	if len(dest) > 0 and dest[-1] != '/': dest = dest + '/'
	 
	packImages(listFiles(path), dest)


if __name__ == "__main__":
	main()