#!/usr/bin/python

filepath='/disk/data/datastage/CPSS_BI_CONSUMERS/CPB_EXPLORATION/input/BCRealEstate/'
prev_line = ''
i=0
with open(filepath+'BCAA_2017_Part14_test.xml','rb') as fin:
    with open(filepath+'BCAA_2017_Part14_test1.xml','wb') as fout:

        for current_line in fin:
                i=i+1
                if current_line.strip().rstrip() != '</OilAndGas>':

                        fout.write(current_line)
                elif prev_line.strip()!= current_line.strip():
                        fout.write(current_line)
                        print ""+str(i)+":"+ current_line

                else:
                        print current_line
                        fout.write(current_line.replace('</OilAndGas>','</OilAndGases>'))

                prev_line = current_line

fin.close()
fout.close()
