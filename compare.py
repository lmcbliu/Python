import csv
data1 = {}
#with open("file1.csv", "rb") as in_file1:
#    reader1 = csv.reader(in_file1)
#    for row1 in reader1:
#        data1[row1[0]] = row1[1]
        

lines = [line.rstrip('\r\n') for line in open("/home/bxl103//lmcbliu/EC24LX4060_Kesa_temp","r")]
result=[]

for x in lines:
    result.append(x.split(' ')[0])


for i, v in enumerate(result):
    data1[i]=v

#print ([x.split(' ')[0] for x in open("/home/bxl103/lmcbliu/EC24LP4060_kerm_temp").readlines()])

print(result)

with open("/home/bxl103/lmcbliu/file2.csv","r") as in_file2:
	with open("/home/bxl103/lmcbliu/EC24LD4060_Kesa_temp.csv","w") as out_file:
		reader2 = csv.reader(in_file2)
		writer = csv.writer(out_file)
		for row2 in reader2:
			if row2[0] in result:
				pass
 #           	row2.append(data1[row2[0]])
			else:
				writer.writerow(row2)