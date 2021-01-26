#!/usr/bin/python
import csv
with open("forum_node.tsv", 'r',encoding='utf-8') as _in:
	with open("clean_forum.tsv",'w',encoding='utf-8') as _out:
		for l in _in.readlines():
			_out.write(l.strip()+"\n")