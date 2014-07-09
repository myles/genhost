#!/usr/bin/env python

import os
import re
import argparse

import requests
from BeautifulSoup import BeautifulSoup

MARVEL_COMIC_BOOK_CHARACTERS_PAGE = 'http://marvel.com/comics/characters'

def main(output):
	r = requests.get(MARVEL_COMIC_BOOK_CHARACTERS_PAGE)
	
	soup = BeautifulSoup(r.text)
	
	character_list = soup.find('div', attrs={'class': 'JCAZList-list'}).findAll('a')
	
	characters = []
	
	for character in character_list:
		name = re.sub(r'\([^)]*\)', '', character.text).strip()
		name = name.split('/')[0]
		name = re.sub(r'[^\w\s-]', '', name)
		characters += [re.sub(r'[-\s]+', '-', name).lower(),]
	
	with open(os.path.abspath(output), 'a') as handler:
		for character in set(characters):
			handler.write("%s\n" % character)
			
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', dest='output', action='store', required=True)
	
	args = parser.parse_args()
	
	main(args.output)