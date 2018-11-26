import os
import sys
reg32=['eax','ecx','edx','ebx','esp','ebp','esi','edi']
reg16=['ax','cx','dx','bx','sp','bp','si','di']
reg8=['al','cl','dl','bl','ah','ch','dh','bh']
regval=['000','001','010','011','100','101','110','111']
regpush=['50','51','52','53','54','55','56','57']
regimm=['C0','C1','C2','C3','C4','C5','C6','C7']
regdword=['A1','8B0D','8B15','8B1D','8B25','8B2D','8B35','8B3D']
regbyte=['A0','8A0D','8A15','8A1D','8A25','8A2D','8A35','8A3D']
cmpreg=['83F8','83F9','83FA','83FB','83FC','83FD','83FE','83FF']
increg32=['40','41','41','41','44','45','46','47']
decreg32=['48','49','4A','4B','4C','4D','4E','4F']
rval=0
fp=open(sys.argv[1],"r")
line=fp.readlines()
total_addr=[]
total_val=[]
valpush=[]
valval=[]
addr=[]
pushval=""
k=0
hexadr=0
hexadr1=0
hexadr2=0	
count=0
count2=0
count3=0
count4=0
i=0
itr=0
while(line[i].find('ain:')<0):
	i+=1;
	itr+=1

for i in range(0,len(line)):
		if(line[i].find(' db ')>0):
			if(line[i].find('"')>0):
				string=line[i]	
				hexadr=count
				total_addr.append(hexadr)
				nm=line[i].split()
				total_val.append(nm[0])
				valpush.append(nm[0])
				left=0
				right=0
				newstring=''
				ele=''
				for m in range(0,len(string)):
					if(string[m]!='\"'):
						left=left+1
					else:
						break
				k=len(string)
				while(string[k-1]!='\"'):
					right=right+1
					k=k-1
				right=len(string)-right
				newstring=string[left:right]
				for k in range(0,len(newstring)):
					if(newstring[k]!='\"'):
						ele=ele+hex(ord(newstring[k]))
				ele=ele.replace("0x","")
				ele=ele.upper()
				if(string.find(",10,0")>0):
					ele=ele+'0A00'
				count=count+len(newstring)
				str4=str(hex(hexadr)).replace("0x","")
				str4='000000'+(str4.upper())
				valval.append(str4)
				if(len(str4)<8):
					str4='0'+str4
				print ("%s    %s\t%s"%(str4,ele,line[i]))
			else:
				addr=[]
				hexadr=count
				total_addr.append(hexadr)
				nm=line[i].split()
				total_val.append(nm[0])
				valpush.append(nm[0])
				str1=line[i].split()
				str2=str1[2].split(',')
				for j in range(0,len(str2)):
					addr.append(hex(int(str2[j])))
					count=count+1
				str3=''.join(addr)
				str3=str3.replace("0x","")
				str3=str3.upper()
				str4=str(hex(hexadr)).replace("0x","")
				str4='000000'+(str4.upper())
				valval.append(str4)
				if(len(str4)<8):
					str4='0'+str4
				print("%s     %s\t%s"%(str4,str3,line[i]))
		
		if(line[i].find(' dq ')>0):
			addr=[]
			hexadr=count
			total_addr.append(hexadr)
			nm=line[i].split()
			total_val.append(nm[0])
			str1=line[i].split()
			str2=str1[2].split(',')
			valpush.append(nm[0])
			for j in range(0,len(str2)):
				addr.append(hex(int(str2[j])))
				addr.append('000000000000')
				count=count+8
			str3=''.join(addr)
			str3=str3.replace("0x","")
			str3=str3.upper()
			str4=str(hex(hexadr)).replace("0x","")
			str4='000000'+(str4.upper())
			valval.append(str4)
			if(len(str4)<8):
					str4='0'+str4
			print("%s     %s\t%s"%(str4,str3,line[i]))
		
		if(line[i].find(' dw ')>0):
			addr=[]
			hexadr=count
			total_addr.append(hexadr)
			nm=line[i].split()
			total_val.append(nm[0])
			str1=line[i].split()
			str2=str1[2].split(',')
			valpush.append(str1[0])
			for j in range(0,len(str2)):
				addr.append(hex(int(str2[j])))
				addr.append('00')
				count=count+2
			str3=''.join(addr)
			str3=str3.replace("0x","")
			str3=str3.upper()
			str4=str(hex(hexadr)).replace("0x","")
			str4='000000'+(str4.upper())
			valval.append(str4)
			if(len(str4)<8):
					str4='0'+str4
			print("%s     %s\t%s"%(str4,str3,line[i]))
		if(line[i].find(' dd ')>0):
			addr=[]
			hexadr=count
			total_addr.append(hexadr)	
			nm=line[i].split()
			total_val.append(nm[0])
			str1=line[i].split()
			str2=str1[2].split(',')
			valpush.append(str1[0])	
			for j in range(0,len(str2)):
				addr.append(hex(int(str2[j])))
				count=count+4
				addr.append('000000')
			str3=''.join(addr)
			str3=str3.replace("0x","")
			str3=str3.upper()

			str4=str(hex(hexadr)).replace("0x","")
			str4='000000'+(str4.upper())
			valval.append(str4)
			if(len(str4)<8):
					str4='0'+str4
			print("%s     %s\t%s"%(str4,str3,line[i]))
		if(line[i].find(' resb ')>0):
			hexadr1=hexadr1+count2
			total_addr.append(hexadr1)
			str1=line[i].split()
			valpush.append(str1[0])							
			if(str1[1]=='resb'):
				count2=(1*int(str1[2]))
			pushval='000000'+str(hex(hexadr1)).replace("0x","")
			valval.append(pushval)
			print("%s    <res %s>\t%s"%(pushval,'000000'+str(hex(count2)).replace("0x",""),line[i]))
		
		if(line[i].find(' resw ')>0): 	
			hexadr1=hexadr1+count2
			total_addr.append(hexadr1)
			str1=line[i].split()
			valpush.append(str1[0])
			if(str1[1]=='resw'):
				count2=(2*int(str1[2]))
			pushval='000000'+str(hex(hexadr1)).replace("0x","")
			valval.append(pushval)
			print("%s    <res %s>\t%s"%(pushval,'000000'+str(hex(count2)).replace("0x",""),line[i]))

		if(line[i].find(' resd ')>0):
			hexadr1=hexadr1+count2
			total_addr.append(hexadr1)
			str1=line[i].split()
			valpush.append(str1[0])
			if(str1[1]=='resd'):
				count2=(4*int(str1[2]))
			pushval='000000'+str(hex(hexadr1)).replace("0x","")
			valval.append(pushval)
			print("%s    <res %s>\t%s"%(pushval,'000000'+str(hex(count2)).replace("0x",""),line[i]))

		if(line[i].find(' resq ')>0):
			hexadr1=hexadr1+count2
			total_addr.append(hexadr1)
			str1=line[i].split()
			valpush.append(str1[0])
			if(str1[1]=='resq'):
				count2=(8*int(str1[2]))
			pushval='000000'+str(hex(hexadr1)).replace("0x","")
			valval.append(pushval)
			print("%s    <res %s>\t%s"%(pushval,'000000'+str(hex(count2)).replace("0x",""),line[i]))
hexadr2=0
count4=0
movaddr=0
for i in range(itr,len(line)):
	if(line[i].find('cmp')>0):
		str1=line[i].split()
		str2=str1[1].split(',')
		hexadr2=count4
		str4=str(hex(hexadr2)).replace("0x","")
		str4='000000'+(str4.upper())
		count4=count4+3
		if(str2[0] in reg32):
			k=reg32.index(str2[0])
			rval=cmpreg[k]+str(hex(int(str2[1]))).replace("0x","").upper()
		print("%s    %s\t%s"%(str4,rval,line[i]))
	if(line[i].find('dec')>0):
		str1=line[i].split()
		hexadr2=count4
		str4=str(hex(hexadr2)).replace("0x","")
		str4='000000'+(str4.upper())
		if str1[1] in reg32:
			count4=count4+1
			k=reg32.index(str1[1])
			print("%s    %s\t%s"%(str4,decreg32[k],line[i]))
		if str1[1] in reg16:
			count4=count4+2
			k=reg16.index(str1[1])
			print("%s    %s\t%s"%(str4,decreg32[k],line[i]))
		if str1[1] in reg8:
			count4=count4+2
			k=reg8.index(str1[1])
			print("%s    %s\t%s"%(str4,decreg32[k],line[i]))

	if(line[i].find('inc')>0):
		str1=line[i].split()
		hexadr2=count4
		str4=str(hex(hexadr2)).replace("0x","")
		str4='000000'+(str4.upper())
		if str1[1] in reg32:
			count4=count4+1
			k=reg32.index(str1[1])
			print("%s    %s\t%s"%(str4,increg32[k],line[i]))
		if str1[1] in reg16:
			count4=count4+2
			k=reg16.index(str1[1])
			print("%s    %s\t%s"%(str4,increg32[k],line[i]))
		if str1[1] in reg8:
			count4=count4+2
			k=reg8.index(str1[1])
			print("%s    %s\t%s"%(str4,increg32[k],line[i]))

	if(line[i].find('dword')>0):
			hexadr2=count4
			str4=str(hex(hexadr2)).replace("0x","")
			str4='000000'+(str4.upper())
			count4=count4+1
			str1=line[i].split()
			str2=str1[1].split(',')
			if(str2[0] in reg32):
				str3=str2[1].split('[')
				dwordval=str3[1][0]
				if dwordval in valpush:
					k=valpush.index(dwordval)
				l=reg32.index(str2[0])
				print("%s    %s\t%s"%(str4,regdword[l]+'['+valval[k]+']',line[i]	))

	if(line[i].find('call')>0):
		if(line[i].find('ain:')>0 or line[i].find('main')>0 or line[i].find('printf')>0 or line[i].find('scanf')>0):
			hexadr2=count4
			str4=str(hex(hexadr2)).replace("0x","")
			str4='000000'+(str4.upper())
			count4=count4+1
			print("%s    %s\t%s"%(str4,"E8(00000000)",line[i]))
	if(line[i].find('pusha')>0 or line[i].find('popa')>0):
			hexadr2=count4
			str4=str(hex(hexadr2)).replace("0x","")
			str4='000000'+(str4.upper())
			count4=count4+1
			if(line[i].find('pusha')>0):
				print("%s    %s\t%s"%(str4,"60",line[i]))
			if(line[i].find('popa')>0):
				print("%s    %s\t%s"%(str4,"61",line[i]))
	if(line[i].find('push')>0):
			str1=line[i].split()
			hexadr2=count4
			str4=str(hex(hexadr2)).replace("0x","")
			str4='000000'+(str4.upper())
			count4=count4+1
			if(len(str1)==2):
				if(str1[1] in valpush):
					k=valpush.index(str1[1])
					print("%s    68[%s]\t%s"%(str4,valval[k],line[i]))

				if(str1[1] in reg32):
					k=reg32.index(str1[1])
					print("%s    %s\t%s"%(str4,regpush[k],line[i]))
					
			if(len(str1)==3):
				if(str1[2] in valpush):
					k=valpush.index(str1[2])
					print("%s    68[%s]\t%s"%(str4,valval[k],line[i]))
			
				if(str1[2] in reg32):
					k=reg32.index(str1[2])
					print("%s    %s\t%s"%(str4,regpush[k],line[i]))
			
	if(line[i].find("mov")>0 or line[i].find("add")>0 or line[i].find("sub")>0 or line[i].find("mul")>0):
			str1=line[i].split()
			str2=str1[1].split(",")
			hexadr2=count4
			k=0
			index1=0
			index2=0
			r32=0
			r16=0
			r8=0
			movaddr=str(hex(count4)).replace("0x","")
			if(len(movaddr)==1):
				movaddr='0000000'+(movaddr)
			else:
				movaddr='000000'+(movaddr)
			k=0
			for k in range(0,len(reg32)):
				if(reg32[k]==str2[0]):
					index1=k
					r32=1
					break
				if(reg16[k]==str2[0]):
					index1=k
					r16=1
					break
				if(reg8[k]==str2[0]):
					index1=k
					r8=1
					break
			if(str2[1] in reg32 or str2[1] in reg16 or str2[1] in reg8):
				j=0
				for j in range(0,len(reg16)):
						if(len(str2)>1):
							if(reg32[j]==str2[1]):
								index2=j
								r32=1
								break
							if(reg16[j]==str2[1]):
								index2=j
								r16=1
								break
							if(reg8[k]==str2[0]):
								index2=j
								r8=1
								break
				
				if(r32==1):
						count4=count4+2
				elif(r16==1):
						count4=count4+3
				else:
						count4=count4+2
				sum1=0
				sum2=0
				val='11'+regval[index2]+regval[index1]
				val1=val[:4]
				val2=val[4:]
				n=len(val1)-1
				k=0
				for k in range(0,len(val1)):
					sum1=sum1+int(val1[k])*pow(2,n-k)
					sum2=sum2+int(val2[k])*pow(2,n-k)
				sum1=hex(sum1)
				sum1=str(sum1).replace("0x","")
				sum2=hex(sum2)
				sum2=str(sum2).replace("0x","")

				if(line[i].find('mov')>0):
					if(r16==1):
						string=('6689'+sum1+sum2).upper()
					else:
						string=('89'+sum1+sum2).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string,line[i]))
				if(line[i].find('add')>0):
					if(r16==1):
						string=('6601'+sum1+sum2).upper()
					else:
						string=('01'+sum1+sum2).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string,line[i]))
				
				if(line[i].find('sub')>0):
					if(r16==1):
						string=('6602'+sum1+sum2).upper()
					else:
						string=('29'+sum1+sum2).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string,line[i]))
				
				if(line[i].find('mul')>0):
					if(r16==1):
						string=('66F7'+sum1+sum2).upper()
					else:
						string=('f7'+sum1+sum2).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string,line[i]))
		
				

			elif(str2[1] in valpush):
				l=reg32.index(str2[0])
				k=valpush.index(str2[1])
				count4=count4+1
				
				if(line[i].find('mov')>0):
					if(r16==1):
						string=('6689'+regimm[l]).upper()
					else:
						string=('89'+regimm[l]).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string+'['+valval[k]+']',line[i]))
				if(line[i].find('add')>0):
					if(r16==1):
						string=('6601'+regimm[l]).upper()
					else:
						string=('81'+regimm[l]).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string+'['+valval[k]+']',line[i]))
				
				if(line[i].find('sub')>0):
					if(r16==1):
						string=('6602'+regimm[l]).upper()
					else:
						string=('29'+regimm[l]).upper()
					print("%s\t%s"%((movaddr).upper(),string+'['+valval[k]+']'))
				
				if(line[i].find('mul')>0):
					if(r16==1):
						string=('66F7'+regimm[l]).upper()
					else:
						string=('f7'+regimm[l]).upper()
					print("%s\t%s\t%s"%((movaddr).upper(),string+'['+valval[k]+']',line[i]))
			else:
				if(line[i].find('dword')<0):
					l=reg32.index(str2[0])
					val=hex(int(str2[1]))
					val=val.replace("0x","").upper()
					count4=count4+1
					if(len(val)==1):
						val='0'+val
					if(line[i].find('mov')>0):
						if(r16==1):
							string=('6689'+regimm[l]).upper()
						else:
							string=('89'+regimm[l]).upper()
						print("%s\t%s\t%s"%((movaddr).upper(),string+val,line[i]))
					if(line[i].find('add')>0):
						if(r16==1):
							string=('6683'+regimm[l]).upper()
						else:
							string=('83'+regimm[l]).upper()
						print("%s\t%s\t%s"%((movaddr).upper(),string+val,line[i]))
					
					if(line[i].find('sub')>0):
						if(r16==1):
							string=('6602'+regimm[l]).upper()
						else:
							string=('29'+regimm[l]).upper()
						print("%s\t%s\t%s"%((movaddr).upper(),string+val,line[i]))
					
					if(line[i].find('mul')>0):
						if(r16==1):
							string=('66F7'+regimm[l]).upper()
						else:
							string=('f7'+regimm[l]).upper()
						print("%s\t%s\t%s"%((movaddr).upper(),string+val,line[i]))
					
				




			
	





		
		
		
		
