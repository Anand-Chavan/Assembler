import os
import re
import sys
os.linesep
fname1=sys.argv[1]
f1=open(fname1,"r")
f2=open("lit.txt","w")
line=f1.readlines()
d=1
num=[]
f2.write("\nLNo\tSNo\tOriginalValue\t\tHex-Value\n")
#print("\nLineNo\tOriginalValue\t\tHex-Value\n")
for i in range(0,len(line)):
	if(i):
			if(line[i].find("\"")>0):
				string=line[i]
				str1=line[i].split()	
				left=0
				right=0
				newstring=''
				ele=''
				for m in range(0,len(string)):
					if(string[m]!='\"'):
						left=left+1
					else:
						break
				g=len(string)
				while(string[g-1]!='\"'):
					right=right+1
					g=g-1
				right=len(string)-right
				newstring=string[left:right]
				for k in range(0,len(newstring)):
					if(newstring[k]!='\"'):
						ele=ele+hex(ord(newstring[k]))
				ele=ele.replace("0x","")
				ele=ele.upper()
				f2.write("%d\t%d\t%s\t\t%s"%(i,d,newstring,ele)+os.linesep)
				d=d+1
				#print("%d\t%s\t\t%s"%(i,newstring,ele))
			elif((line[i].find(' db '))>0 or (line[i].find(' dw '))>0 or (line[i].find(' dq '))>0 or (line[i].find(' dd '))>0 or (line[i].find(' resb '))>0 or (line[i].find(' resw '))>0  or(line[i].find(' resd '))>0 or (line[i].find(' resq '))>0 ):
					str1=line[i].split()
					ele=''
					if(str1[2].find(',')>0):
						str2=str1[2].split(',')
						if(len(str2)>1):
							for j in range(0,len(str2)):
								ele=ele+hex(int(str2[j]))
					else:
						str2=str1[2]
						ele=hex(int(str2))
					ele=ele.replace("0x","")
					ele=ele.upper()
					f2.write("%d\t%d\t%s\t\t%s"%(i,d,str2,ele)+os.linesep)
					d=d+1
					#print("%d\t%s\t\t%s"%(i,str2,ele))
			else:
				import re  
				text = line[i]  
				num= re.findall('\\d+', text)
				if(num!=[]):
					f2.write("%d\t%d\t%d\t\t%x"%(i,d,int(num[0]),int(num[0]))+os.linesep)
					d=d+1
				'''if(line[i].find(',')>0):
					str1=line[i]
					str2=str1.split(',')
					num=map(int, re.findall(r'\d+', str2[1]))
					print(num)
					if(num!=[]):
							#str2=str(hex(num[0])).replace("0x","")
							f2.write("%d\t%d\t%d\t\t%x"%(i,d,num[0],num[0])+os.linesep)
							d=d+1
							#print("%d\t%d\t\t%s"%(i,num[0],str2))'''
					

