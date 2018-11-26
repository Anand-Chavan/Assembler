import os
import sys
reg32=['eax','ecx','edx','ebx','esp','ebp','esi','edi']
reg16=['ax','cx','dx','bx','sp','bp','si','di']
reg8=['al','cl','dl','bl','ah','ch','dh','bh']
regval1=['32R0','32R1','32R2','32R3','32R4','32R5','32R6','32R7']
regval2=['16R0','16R1','16R2','16R3','16R4','16R5','16R6','16R7']
regval3=['8R0','8R1','8R2','8R3','8R4','8R5','8R6','8R7']
count=0
i=0
flag=0
literal=[]
symbol=[]
sym=[]
fptr=open("intermediate.txt","w")
name=sys.argv[1]
if(os.system('python 17109-literal-table.py %s'%(name))==0 and os.system('python 17109-symbol_table.py %s'%(name))==0):
	f=open(name,"r")
	line=f.readlines()
	while((line[i].find('ain:')<0)):
		count=count+1
		i=i+1
	for i in range(0,count):
		fptr.write((line[i])+os.linesep)
	f1=open('lit.txt','r')
	line1=f1.readlines()
	for j in range(2,len(line1)):
		str1=line1[j].split()
		literal.append(str1[2])		
	
	f2=open('sym.txt','r')
	line2=f2.readlines()
	for j in range(1,len(line2)):
		str2=line2[j].split()
		symbol.append(str2[0])
	f3=open(name,'r')
	line3=f3.readlines()
	for j in range(count,len(line3)):
		flag=0
		string=line3[j]
		str3=line3[j].split()
		if(line3[j].find('dword')>0):
			str4=line3[j].split('[')
			str4=str4[1][:-2]
			str6=str4[0]
			if(len(str6)>=1):
				if(str6 in symbol):
					k=symbol.index(str6)
					line3[j]=line3[j].replace(str(str6),'sym#'+str(k))
		if(len(str3)>=1):
			if(line[j].find(':')>0):
				str6=str3[0]
				lth=len(str6)-1
				str6=str6[0:lth]
				if(str6 in symbol):
					k=symbol.index(str6)
					line3[j]=line3[j].replace(str6,'sym#'+str(k))
		if(len(str3)==2):
			if(line3[j].find(',')>0):
				str4=str3[1].split(',')
				str3=str4
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'sym#'+str(k))
					
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
			else:
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'sym#'+str(k))
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
			
		if(len(str3)==3):
			if(line3[j].find(',')>0):
				str4=str3[2].split(',')
				if(len(str4)>1):
					if(str4[1] in symbol):
						k=symbol.index(str4[1])
						line3[j]=line3[j].replace(str3[1],'sym#'+str(k))
						
					if(str4[1] in literal):
						k=literal.index(str4[1])
						line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
					if(str4[0] in reg32):
						k=reg32.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval1[k]))
					if(str4[1] in reg32):
						k=reg32.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval1[k]))
					if(str4[0] in reg16):
						k=reg16.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval2[k]))
					if(str4[1] in reg16):
						k=reg16.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval2[k]))
					if(str4[0] in reg8):
						k=reg8.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval3[k]))
					if(str4[1] in reg8):
						k=reg8.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval3[k]))
						
			else:
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'sym#'+str(k))
				
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
				if(str3[0] in symbol):
					k=symbol.index(str3[0])
					line3[j]=line3[j].replace(str3[0],'sym#'+str(k))
				
				elif(str3[0] in literal):
					k=literal.index(str3[0])
					line3[j]=line3[j].replace(str3[0],'LIT#'+str(k))
				if(str3[2] in symbol):
					k=symbol.index(str3[2])
					line3[j]=line3[j].replace(str3[2],'sym#'+str(k))
				
				elif(str3[2] in literal):
					k=literal.index(str3[2])
					line3[j]=line3[j].replace(str3[2],'LIT#'+str(k))
			
		
		str3=line3[j].split()
		if(line[j].find(',')>0):
				str4=str3[1].split(',')
				if(len(str4)>1):
					if(str4[0] in reg32):
						k=reg32.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval1[k]))
					if(str4[1] in reg32):
						k=reg32.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval1[k]))
					if(str4[0] in reg16):
						k=reg16.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval2[k]))
					if(str4[1] in reg16):
						k=reg16.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval2[k]))
					if(str4[0] in reg8):
						k=reg8.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval3[k]))
					if(str4[1] in reg8):
						k=reg8.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval3[k]))
		else:
			if(len(str3)==2):
				if(str3[1] in reg32):
					k=reg32.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval1[k]))
				if(str3[1] in reg16):
					k=reg16.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval2[k]))
				if(str3[1] in reg8):
					k=reg32.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval3[k]))
			if(len(str3)==3):
				if(str3[2] in reg32):
					k=reg32.index(str3[2])
					line3[j]=line3[j].replace(str(str3[2]),str(regval1[k]))
				if(str3[2] in reg16):
					k=reg16.index(str3[2])
					line3[j]=line3[j].replace(str(str3[2]),str(regval2[k]))
				if(str3[2] in reg8):
					k=reg32.index(str3[2])
					line3[j]=line3[j].replace(str(str3[2]),str(regval3[k]))
			
		
		fptr.write("%s"%(line3[j])+os.linesep)

































































































			
			
		
				
