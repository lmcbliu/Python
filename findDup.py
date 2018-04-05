'''
Created on Apr 5, 2018

@author: beaul
'''


with open("file1.txt", "r") as first_file, open("file2.txt", "r") as second_file, open('duplicate.txt','w') as dst:
    file1 = first_file.readlines()
    file2 = second_file.readlines()
    length1 = len(file1)
    length2 = len(file2)
    for i in range(length1):
        for j in range(length2):
            if file1[i].rstrip('\n')!= file2[j].rstrip('\n'):
                if  file1[i].rstrip('\n').lower() in file2[j].rstrip('\n').lower():
                    print(file1[i].rstrip('\n'))
                    print(file2[j].rstrip('\n'))
                