import csv, re

while True:
	try:
		'''
		On récupère le path grâce à une regex et on le décompose en 3 strings : 
			- path
			- filename
			- extension
		'''
		fullpath = re.findall(r"((?:[A-Z]:/|\./|/)?(?:[^.]+/)*)([^/]+)(\.csv)", input("Enter path to CSV :\n").replace('\\', '/'))[0]
		print(fullpath)

		src = ''.join(map(str,fullpath))
		print(src)

		
		filename = fullpath[-2]
		ext = fullpath[-1]
		path = fullpath[0]
		
		with open(src,'r') as csvFile, open('{}{}.tsv'.format(path, filename), 'w+') as tsvFile:
			csvFile = csv.reader(csvFile)
			tsvFile = csv.writer(tsvFile, delimiter='\t')

			for row in csvFile:
				tsvFile.writerow(row)

		print('\n-----\nOutput file => {}.tsv at {}\n'.format(filename, path))
		break

	except IndexError:
		print("\n–––\nMake sure the full path including filename extension is correct!\n–––\n")
		pass
	except FileNotFoundError:
		print("\n–––\nFile not found!\n–––\n")