# methods learned
# csv.reader(file object name)	(for reading a csv file)
# csv.writer(name of the file object to be written)   (for writing in a different csv file)
# csv.DictReader(file object name)   (for reading a file in a dictionary way)
# csv.DictWriter(name of the file object to be written)  (for writng in a different csv file)
# file_object.writeheader()   (if you wanna keep those headers in the writing file)

import csv
with open ('cms.csv','r') as csv_file:
	'''
	csv_r=csv.reader(csv_file)
	# next(csv_r)	#loops over first line
	
	with open('new_f.csv','w') as n_file:
		csv_w=csv.writer(n_file,delimiter='-')  # same csv file separated by commas
	
		for line in csv_r:
			print(line[0])
			print(line)
			print('\n')
			csv_w.writerow(line)
			
	'''
	print('\nusing DictReader\n')
	
	csv_dr=csv.DictReader(csv_file) # advantage is we can use the file as key value pairs

	with open('new_f2.csv','w') as n2_file:
		field_names=['summary','headline','vid_link']
		csv_dw=csv.DictWriter(n2_file,fieldnames=field_names)  # same csv file separated by commas

		csv_dw.writeheader()   # if you wanna keep those headers
	
		for line in csv_dr:
			print(line)
			print(line['headline'])
			print('\n')
			csv_dw.writerow(line)
