import csv
import datetime
import string

from datetime import datetime

VT = int(input("Anzahl der Verteiler angeben: "))

ts = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()
print (ts)

gcsv = open('Glabel-CSV-%s.csv' %ts, "w+")
fnames = ['A']
writer = csv.DictWriter(gcsv,fieldnames=fnames)
writer.writeheader

a = string.ascii_uppercase
print(a)
i = 1
while i <= VT:
	P = int(input("Anzahl der Panele des VT%i angeben: " %i))
	j = 0
	while j < P:
		k = 1
		while k <= 24:
			string = '%s%i VT%i %s%i'% (a[j], k, i, a[j], k+1)
			print(string)
			writer.writerow({'A' : string})
			k = k + 2
		j = j + 1
	i = i + 1

gcsv.close()



