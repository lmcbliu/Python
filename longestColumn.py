#! /usr/bin/python

# This program is to read the longest column length for all columns in the file
# This program works on Python version 2.6 (our server has only this version)
# Author : Bo Liu (bxl103)
# Date 2017-10-19

import csv, sys

lengths={}

input_filepath = raw_input("Please Enter file path and file name: ")
delimit = raw_input("Please enter delimiter: ")
firstLine = raw_input("First Line is column? enter 1 when yes or 2 when no: ")

try:
        with open(input_filepath, 'rt') as f:
			
			if firstLine== '1':
				reader = csv.DictReader(f, delimiter=delimit)	
				for index,row in enumerate(reader):
					if index == 0:
						for heading in row.keys():
							lengths[heading] = 0
					for column in row.keys():
						if (len(row[column]) > lengths[column]):
							lengths[column] = len(row[column]) 
				print (lengths)
			
			elif firstLine== '2':
				rowNumber=0
				columnName =[]
				for raw in f:
					if rowNumber==0:
						j=0
						for columns in raw.strip().split(delimit):
							j=j+1
							columnName.append('Column'+str(j))
					break		
				print(columnName)			
				reader = csv.DictReader(f, fieldnames=columnName,delimiter=delimit)	
					
				for index,row in enumerate(reader):
					if index ==0:
						for heading in row.keys():
							lengths[heading] = 0
					for column in row.keys():
						if (len(row[column]) > lengths[column]):
							lengths[column] = len(row[column]) 
				print (lengths)
			

        f.close()
except IOError as e:
        print "file is not exist"


max(len(str(x)) for x in line) for line in zip(*foo)]


