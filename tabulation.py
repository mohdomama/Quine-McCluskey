def printing(mainList):
	for string in [x[0] for x in mainList]:
		count=-1
		for i in string:
			count+=1
			if i=='0':
				print(chr(ord('a')+count)+"'",end="")
			elif i =="1":
				print(chr(ord('a')+count),end="")
		print("  +  ",end="")
	print('0')


def categorize(min_terms,variables):
	min_terms_categorised={}
	
	for i in range (variables+1):
		min_terms_categorised[i]=[]

	for i in min_terms:
		min_terms_categorised[i.count("1")].append([i,[int(i,2)]])

	return min_terms_categorised


def inputData():
	variables=int(input("Enter the number of variables:\n"))
	min_terms=[bin(int(x))[2:].zfill(variables) for x in input("Enter the minterms:\n").split()]
	min_terms_categorised = categorize(min_terms,variables)
	return variables,min_terms_categorised


def check(element1,element2):
	count=0
	combined=[]
	for i in range (len(element1[0])):
		combined.append(element1[0][i])
		if element2[0][i]!=element1[0][i]:
			combined[i]='-'
			count+=1
	if count>1:
		return False
	else:
		return ["".join(combined),element1[1]+element2[1]]



def getPrimeImplicants(terms,number,prime_implicants):
	new_terms={}
	recursion=0
	used_terms=[]
	for i in range (number):
		new_terms[i]=[]
	for i in range (number):
		for element1 in terms[i]:
			flag=0
			for element2 in terms[i+1]:
					combined=check(element1,element2)
					if combined:
						recursion=1
						flag=1
						new_terms[i].append(combined)
						if element1[0] not in used_terms:
							used_terms.append(element1[0])
						if element2[0] not in used_terms:
							used_terms.append(element2[0 ])

			if flag==0:
				if element1[0] not in used_terms and element1[0] not in [x[0] for x in prime_implicants]:
					prime_implicants.append(element1)

	for i in terms[number]:
		if i[0] not in used_terms and i[0] not in [x[0] for x in prime_implicants]:
			prime_implicants.append(i)

	if not recursion:
		return
	else:
		getPrimeImplicants(new_terms,number-1,prime_implicants)



def selectImplicants(table,selected_implicants):
	minimum=min([len(table[i]) for i in table])
	minimum=[x for x in table if len(table[x])==minimum]
	deletion=[]
	for i in minimum:
		maximum = [x for x in table[i] if len(x[1])==max(len(j[1]) for j in table[i])]
		for k in maximum:
			for j in k[1]:
				if j not in deletion:
					deletion.append(j)
			if k not in selected_implicants:
				selected_implicants.append(k)

	for i in deletion:
		del table[i]
	for i in table:
		for k in table[i] :
			for j in deletion:
				if j in k[1]:
					k[1].remove(j)



def getEssential(table,essential_implicants):

	for i in [x for x in table if len(table[x])==1]:
		if table[i][0] not in essential_implicants:
			essential_implicants.append(table[i][0])
		del table[i]


def getAllSelected(POS,temp,allSelected,index):
	if index==len(POS):
		temp1=temp+[]
		#print("reached:" , temp1)
		allSelected.append(temp1)
		return
	else:
		for i in POS[index]:
			if i not in temp:
				temp.append(i)
				getAllSelected(POS,temp,allSelected,index+1)
				temp.remove(i)
			else:
				getAllSelected(POS,temp,allSelected,index+1)


def petrickMethod(table,selected_implicants):
	temp=[]
	POS=[]
	allSelected=[]
	for i in table:
		POS.append(table[i])

	getAllSelected(POS,temp,allSelected,0)
	for i in allSelected:
			print (i)

	for i in allSelected:
		if len(i)==min([len(x) for x in allSelected]):
			selected_implicants.append(i)

def minimalize(prime_implicants,min_terms_categorised):
	selected_implicants=[]
	table={}
	essential_implicants=[]
	for i,j in min_terms_categorised.items():
		for k in j:
			table[k[1][0]]=[]

	for i in prime_implicants:
		for j in i[1]:
			table[j].append(i)

	getEssential(table,essential_implicants)

	printing(essential_implicants)
	
	for i in table:
		for j in table[i]:
			if j in essential_implicants:
				table[i].remove(j)

	for i in essential_implicants:
		for j in i[1]:
			if j in [x for x in table]:
				del table[j]

	for i in table:
		print (i," : ",table[i])

	petrickMethod(table,selected_implicants)
	#print (selected_implicants)

	#while len(table):
	#	selectImplicants(table,selected_implicants)
	return essential_implicants,selected_implicants




def main():
	prime_implicants=[]

	variables,min_terms_categorised = inputData()	
	getPrimeImplicants(min_terms_categorised,variables,prime_implicants)	
	essential_implicants,selected_implicants= minimalize(prime_implicants,min_terms_categorised)

	print("\nThe prime implicants are:")
	for i in prime_implicants:
		print(i)

	print("\nThe selected prime implicants are:")
	for i in selected_implicants:
		print(i)

	print("\nThe essential implicants are:")
	for i in essential_implicants:
		print(i)


	for i in selected_implicants:
		for j in i:
			essential_implicants.append(j)
			printing(essential_implicants)
			essential_implicants.remove(j)
	#printing(selected_implicants)
	'''
	print("\nThe function is:")
	for i in selected_implicants:
		if i[0]=="-"*variables:
			print("1 + ",end='')
		else:
			printing(i[0])
	print("0")
	'''
if __name__=="__main__":
	main() 





