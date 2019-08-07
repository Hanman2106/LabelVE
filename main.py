import csv
import datetime
import string

from datetime import datetime

vt = int(input("Anzahl der Verteiler angeben: "))

ts = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()

gcsv = open('Glabel-CSV-%s.csv' %ts, "w+")
fnames = ['A']
writer = csv.DictWriter(gcsv,fieldnames=fnames)
writer.writeheader

a = string.ascii_uppercase
i = 1
while i <= vt:
	p = int(input("Anzahl der Panele des VT%i angeben: " %i))
	j = 0
	while j < p:
		k = 1
		ports = int(input("Anzahl der ports des Panels %s angeben: " %a[j]))
		dosen = (input("Handelt es sich bei den Ports des Panels %s um Doppeldosen? (ja/nein): " %a[j]))		
		while k <= ports:
			if dosen == 'ja':
				string = '%s%i VT%i %s%i'% (a[j], k, i, a[j], k+1)
				k = k + 2
			elif dosen == 'nein':
				string = 'VT%i %s%i'% (i, a[j], k)
				k = k + 1
			print(string)
			writer.writerow({'A' : string})
		j = j + 1
	i = i + 1

gcsv.close()

