def printing(mainList,char):
	'''Prints a boolean function with variables as a,b,c..
	
	Args:
		mainList: A list of lists. Each list should be a string of the form '1's and '0's representing a term of the funtion.
		char: It is the character with which two terms are seperated. e.g- '+' or ','
	'''
	for string in mainList:
		count=-1
		for i in string:
			count+=1
			if i=='0':
				print(chr(ord('a')+count)+"'",end="")
			elif i =="1":
				print(chr(ord('a')+count),end="")
		print("  "+char+"  ",end="")
	print("\b\b\b \n")


def categorize(min_terms,variables):
	''' Categorises minterms on the basis of number of '1's

	Args:
		min_terms: A lsit of min terms. Each item is a binary number string e.g-"1001".
		variables: The number of variables in the function

	Returns:
		min_terms_categorized: A dictionary with number of '1's as keys and a list of minterms as values with the same number of '1's as the key.
	'''
	min_terms_categorised={}
	
	for i in range (variables+1):
		min_terms_categorised[i]=[]

	for i in min_terms:
		min_terms_categorised[i.count("1")].append([i,[int(i,2)]])

	return min_terms_categorised


def inputData():
	'''Takes input. i.e- variables, minterms. Both integer values.

	Returns:
		variables: Number of variables in function.
		min_terms_categorized: A dictionary with number of '1's as keys and a list of minterms as values with the same number of '1's as the key.
	
	'''
	
	
	return variables,min_terms_categorised


def check(element1,element2):
	'''Checks if the two terms differ by only one place.
	
	Args:
		element1: A list with first element a string of "1"s and "0"s and "-"s
		element2: A list with first element a string of "1"s and "0"s and "-"s
		
	Returns:
		False - is terms differ by more than 1
		A string of "1"s and "0"s and "-"s otherwise.
	'''
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
	'''

	Args:
		

	Returns:
	
	'''
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


def getEssential(table,essential_implicants):
	'''

	Args:
		

	Returns:
	
	'''

	for i in [x for x in table if len(table[x])==1]:
		if table[i][0] not in essential_implicants:
			essential_implicants.append(table[i][0])
		del table[i]


def getAllSelected(POS,temp,allSelected,index):
	'''

	Args:
		

	Returns:
	
	'''
	if index==len(POS):
		temp1=temp+[]
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
	'''

	Args:
		

	Returns:
	
	'''
	temp=[]
	POS=[]
	allSelected=[]
	for i in table:
		POS.append(table[i])

	getAllSelected(POS,temp,allSelected,0)

	for i in allSelected:
		if len(i)==min([len(x) for x in allSelected]):
			if i not in selected_implicants:
				selected_implicants.append(i)

def getcount(mainList):
	'''

	Args:
		

	Returns:
	
	'''
	count =0
	for string in [x[0] for x in mainList]:
		for i in string:
			if i=='0' or i=='1':
				count+=1

	return count

def getminimal(selected_implicants):
	'''

	Args:
		

	Returns:
	
	'''
	minimal_implicants=[]
	minimum=999999
	for i in selected_implicants:
		if getcount(i)<minimum:
			minimum=getcount(i)

	for i in selected_implicants:
		if getcount(i)==minimum:
			minimal_implicants.append(i)

	return minimal_implicants

def minimalize(prime_implicants,min_terms_categorised):
	'''

	Args:
		

	Returns:
	
	'''
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

	for i in essential_implicants:
		for j in i[1]:
			if j in [x for x in table]:
				del table[j]

	petrickMethod(table,selected_implicants)
	minimal_implicants=getminimal(selected_implicants)
	
	return essential_implicants, minimal_implicants


def tabulation(variables, min_terms):
	prime_implicants = []
	functions = []

	min_terms=[bin(int(x))[2:].zfill(variables) for x in min_terms]
	min_terms_categorised = categorize(min_terms,variables)

	getPrimeImplicants(min_terms_categorised,variables,prime_implicants)	
	essential_implicants,selected_implicants = minimalize(prime_implicants,min_terms_categorised)

	for i in selected_implicants:
		functions.append( essential_implicants+i )


	prime_implicants = [x[0] for x in prime_implicants]
	essential_implicants = [x[0] for x in essential_implicants]

	for i in range (len(functions)):
		functions[i] = [x[0] for x in functions[i]]

	return prime_implicants, essential_implicants, functions


def main():
	variables = int(input("Enter the number of variables:\n"))
	min_terms = [int(x) for x in input("Enter the minterms (space seperated) :\n").split()]

	prime_implicants, essential_implicants, functions = tabulation(variables, min_terms)

	print("\nThe prime implicants are:")
	printing(prime_implicants,',')

	print("\nThe essential implicants are:")
	printing(essential_implicants,',')

	print("\nThe possible functions are:")
	for i in functions :
		printing(i,'+')



		
	
if __name__=="__main__":
	main() 