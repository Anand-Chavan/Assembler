import sys
import os
fname=sys.argv[1]
startindex=0
endindex=0
arr=[]
macroname=[]
a=[]
j=0
f1=open(fname,"r")
f2=open("macro-expantion.txt","w")
l1=f1.readlines()
for k in range(0,len(l1)):
	i=k
	if(l1[i].find("macro")>0 and l1[i].find("endmacro")<0):
		str1=l1[i].split()
		macroname.append(str1[1])
		arr=[]
		j=i+1
		while(l1[j].find("endmacro")<0):
			arr.append(l1[j])
			j=j+1
		a.append(arr)

i=0
k=0
while(i<len(l1)):
		if(l1[i].find("macro")>0 and l1[i].find("endmacro")<0):
			while(l1[i].find("endmacro")<0):
				i=i+1
			i=i+1
		else:
			f2.write("%s"%(l1[i]))
			i=i+1




		

			
			
	
	
	
		
		
		
	
