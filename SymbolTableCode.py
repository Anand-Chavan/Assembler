import os
import sys
#os.system('python 17109-literal-table.py sys.argv[1]')
fptr=open("lit.txt","r")
l=fptr.readlines()
lit=[]
label1=[]
label2=[]
for g in range(2,len(l)):
	s=l[g].split()
	if(len(s)>1):
		lit.append(s[0])
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
'''# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) '''
os.linesep
size=['0']
size1=['0']
k=0
j=0
addr=0
chk=0
count=0
db=1
flag=0
dw=2
dd=4
dq=8
resb=1
resw=2
resd=4
resq=8
fname1=sys.argv[1]
fp=open(fname1,"r")
f=open("sym.txt","w")
#print("\nName\tSize\tTotal\tSym-Lab\t\tdef-undef\tAddress\t\tValue\n")
f.write("Name\tSize\tTotal\tSym-Lab\t\tdef-undef\tAddress\t\tValue"+ os.linesep)
line=fp.readlines()
for i in range(0,len(line)):
	if(line[i].find('jmp')>0 or line[i].find('jz')>0 or line[i].find('jnz')>0 or line[i].find('je') >0 or line[i].find('neq')>0):
		str1=line[i].split()	
		str2=str1[1]
		label1.append(str2)
	if(line[i].find(':')>0):
		str1=line[i].split()
		if(len(str1)>1):	
			str2=str1[0][:-1]
			label2.append(str2)
	'''if(line[i].find('extern')>0):
		str1=line[i].split()
		if(line[i].find(',')>0):
			str2=str1.split(',')
			for j in range(0,len(str2)):
				label1.append(str1[j])	
		else:
			label1.append(str1[1])	'''
		
label1=Remove(label1)
if 'main' in label2:	
	label2.remove('main')
for i in range(0,len(line)):
	if(i):
		'''if(line[i].find("global")>0 or line[i].find("extern")>0 ):
			if(line[i].find(',')>0):
				str1=line[i].split()
				str2=str1[1].split(',')
				print("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str2[0],'NA','NA','L','D','NA','NA'))
				print("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str2[1],'NA','NA','L','D','NA','NA'))
				f.write("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str2[0],'NA','NA','L','D','NA','NA')+os.linesep)
				print("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str2[1],'NA','NA','L','D','NA','NA'))
			else:
				str1=line[i].split()
				print("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[1],'NA','NA','L','D','NA','NA'))
				f.write("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[1],'NA','NA','L','D','NA','NA')+os.linesep)'''
		if(i):
			if(line[i].find("\"")>0):
				string=line[i]
				str1=line[i].split()	
				addr=size[k]
				k=k+1
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
				size.insert(k,(db*len(newstring)+int(addr)))
				if(str(i) in lit):
					#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],db,len(newstring),'S','D',addr,i))
					f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],db,len(newstring),'S','D',addr,i)+ os.linesep)
				else:
					#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],db,len(newstring),'S','D',addr,"-"))
					f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],db,len(newstring),'S','D',addr,"-")+ os.linesep)
				
			else:
				if((line[i].find(' db '))>0):
					str1=line[i].split()
					str2=str1[2].split(',')
					addr=size[k]
					k=k+1
					size.insert(k,(db*len(str2)+int(addr)))
					if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],db,len(str2),'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],db,len(str2),'S','D',addr,i)+ os.linesep)
					else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],db,len(str2),'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],db,len(str2),'S','D',addr,"-")+ os.linesep)
				if((line[i].find(' dw '))>0):
					str1=line[i].split()
					str2=str1[2].split(',')
					addr=size[k]
					k=k+1
					size.insert(k,(dw*len(str2)+int(addr)))
					if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dw,len(str2),'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dw,len(str2),'S','D',addr,i)+ os.linesep)
					else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dw,len(str2),'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dw,len(str2),'S','D',addr,"-")+ os.linesep)
				if((line[i].find(' dq '))>0):
					str1=line[i].split()
					str2=str1[2].split(',')
					addr=size[k]
					k=k+1
					size.insert(k,(dq*len(str2)+int(addr)))
					if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dq,len(str2),'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dq,len(str2),'S','D',addr,i)+ os.linesep)
					else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dq,len(str2),'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dq,len(str2),'S','D',addr,"-")+ os.linesep)
				if((line[i].find(' dd '))>0):
					str1=line[i].split()
					str2=str1[2].split(',')
					addr=size[k]
					k=k+1
					cval=dd*len(str2)+int(addr)
					size.insert(k,cval)
					if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dd,len(str2),'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],dd,len(str2),'S','D',addr,i)+ os.linesep)
					else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dd,len(str2),'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],dd,len(str2),'S','D',addr,"-")+ os.linesep)
		if(i):
			if((line[i].find(' resb '))>0):
				str1=line[i].split()
				addr1=size1[j]
				j=j+1
				k=k+1
				size1.insert(k,(resb*len(str1[2])+int(addr1)))
				if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resb,len(str2),'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resb,len(str2),'S','D',addr1,i)+ os.linesep)
				else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resb,len(str2),'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resb,len(str2),'S','D',addr1,"-")+ os.linesep)
			if((line[i].find(' resd '))>0):
				str1=line[i].split()
				addr1=size1[j]
				j=j+1
				k=k+1
				size1.insert(k,(resd*len(str1[2])+int(addr1)))
				if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resd,str1[2],'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resd,str1[2],'S','D',addr1,i)+ os.linesep)
				else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr1,"-")+ os.linesep)
			if((line[i].find(' resw '))>0):
				str1=line[i].split()
				addr1=size1[j]
				j=j+1
				k=k+1
				size1.insert(k,(resw*len(str1[2])+int(addr1)))
				if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resw,str1[2],'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resw,str1[2],'S','D',addr1,i)+ os.linesep)
				else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr1,"-")+ os.linesep)
			if((line[i].find(' resq '))>0):
				str1=line[i].split()
				addr1=size1[j]
				j=j+1
				k=k+1
				size1.insert(k,(resq*len(str1[2])+int(addr1)))
				if(str(i) in lit):
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resq,str1[2],'S','D',addr,i))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\tLIT=%d\t"%(str1[0],resq,str1[2],'S','D',addr1,i)+ os.linesep)
				else:
						#print("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr,"-"))
						f.write("%s\t%d\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(str1[0],resq,str1[2],'S','D',addr1,"-")+ os.linesep)
for h in range(0,len(label1)):
	if(label1[h] in label2):
		f.write("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(label1[h] ,'NA','NA','L','D','-','NA')+os.linesep)
	else:
		f.write("%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t"%(label1[h] ,'NA','NA','L','U','-','NA')+os.linesep)
					
		'''if(i):
			if(line[i].find('jmp')>0 or line[i].find('jz')>0 or line[i].find('jnz')>0 or line[i].find('je') >0 or line[i].find('neq')>0):
				str1=line[i].split()	
				str2=str1[1]
				label.append(str2)
				

				str2=str2+':'
				flag=0
				fptr=open(fname1,"r")
				itr=fptr.readlines()
				for j in range(0,len(itr)):
					if(line[j].find(':')>0):
						str3=line[j].split()
						if(str3[0]==str2):
							flag=1;
							break
				if(flag==1):
					#print("%s\t%s\t%s\t%s\t\t%s\t\t%x\t\t%s\t"%(str1[1],'NA','NA','L','D',j,'NA'))
					f.write("%s\t%s\t%s\t%s\t\t%s\t\t%x\t\t%s\t"%(str1[1],'NA','NA','L','D',j,'NA')+os.linesep)
				else:
					#print("%s\t%s\t%s\t%s\t\t%s\t\t%x\t\t%s\t"%(str1[1],'NA','NA','L','U',j,'NA'))
					f.write("%s\t%s\t%s\t%s\t\t%s\t\t%x\t\t%s\t"%(str1[1],'NA','NA','L','U',j,'NA')+os.linesep)'''

















