from csv import DictReader

data_rdr = DictReader(open('data/unicef/mn.csv','rt'))
header_rdr = DictReader(open('data/unicef/mn_headers.csv', 'rt'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]

new_rows = []
