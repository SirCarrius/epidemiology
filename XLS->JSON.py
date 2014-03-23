import xlrd, json

from pprint import pprint
probability_table = {}

filename = 'conditional_token_age.xls'
workbook = xlrd.open_workbook(filename)


for sheet in workbook.sheet_names():
	worksheet = workbook.sheet_by_name(sheet)

	probability_table[sheet] = {}
	#Skip first 3 rows
	nrows = worksheet.nrows-1
	for i in range(3,nrows):
		
		word,r= tuple(worksheet.row_values(i)[:2])
		probability_table[sheet][word] = r

		word,r = tuple(worksheet.row_values(i)[-3:-1])
		probability_table[sheet][word] = r

pprint(probability_table.keys())
json.dump(probability_table,open('conditional_probability.json','wb'))