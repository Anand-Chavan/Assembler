import os 
import sys
name=sys.argv[1]
l=sys.argv[2]

if(l=='-i'):
	os.system('python3 intermediate-code.py %s'%(name))
	print("*******************INTERMEDIATE CODE****************")
	f=open("intermediate.txt","r")
	line=f.readlines()
	for i in range(0,len(line)):
		print(line[i])

if(l=='-s'):
	os.system('python3 17109-literal-table.py %s'%(name))
	os.system('python3 17109-symbol_table.py %s'%(name))
	print("*******************SYMBOL TABLE****************")
	f=open("sym.txt","r")
	line=f.readlines()
	for i in range(0,len(line)):
		print(line[i])
	

if(l=='-l'):
	os.system('python3 17109-literal-table.py %s'%(name))
	os.system('python3 17109-symbol_table.py %s'%(name))
	print("*******************LITERAL TABLE****************")
	f=open("lit.txt","r")
	line=f.readlines()
	for i in range(0,len(line)):
		print(line[i])

if(l=='-lst'):
	print("*******************LST FILE****************")
	os.system('python3 17109-lst-generator.py %s'%(name))	

if(l=='-macro'):
	os.system('python3 macro-table.py %s'%(name))
	f=open("mnt.txt","r")
	line=f.readlines()
	for i in range(0,len(line)):
		print(line[i])


