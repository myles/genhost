import os

with open(os.path.abspath('../servers-wordlist'), 'r') as handler:
	server_wordlist = handler.read().split()

with open(os.path.abspath('../workstations-wordlist'), 'r') as handler:
	workstation_wordlist = handler.read().split()

results = set(server_wordlist).difference(set(workstation_wordlist))

with open(os.path.abspath('../servers-wordlist'), 'w') as handler:
	for r in set(results):
		handler.write("%s\n" % r)