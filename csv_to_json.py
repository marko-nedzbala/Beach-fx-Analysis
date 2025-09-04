import csv
import json


csv_file = open('des_s2.csv', 'r')
json_file = open('de_s2.json', 'w')

field_names = ('LotExtID', 'LotDesc', 'DEExtID', 'DEDesc', 'DEType', 'Ftype', 'Ctype', 'Atype', 'StructMin', 'StructML', 'StructMax',
               'ContentMin', 'ContentML', 'ContentMax', 'DEWidth', 'DELength', 'FFEMin', 'FFEML', 'FFEMax', 'NumOfFloor', 'TBuildMin',
               'TBuildML', 'TBuildMax', 'BuildNum', 'DEActive', 'RepPtN', 'RepPtE' )
reader = csv.DictReader(csv_file, field_names)
for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')


