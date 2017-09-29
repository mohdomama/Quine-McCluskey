def categorize(min_terms,variables):
	min_terms_categorised={}
	
	for i in range (variables+1):
		min_terms_categorised[i]=[]

	for i in min_terms:
		min_terms_categorised[i.count("1")].append(i)

	return min_terms_categorised


def inputData():
	variables=int(input("Enter the number of variables:\n"))
	min_terms=[bin(int(x))[2:].zfill(variables) for x in input("Enter the minterms:\n").split()]
	min_terms_categorised = categorize(min_terms,variables)
	return variables,min_terms_categorised


def check(element1,element2):
	count=0
	combined=[]
	for i in range (len(element1)):
		combined.append(element1[i])
		if element2[i]!=element1[i]:
			combined[i]='-'
			count+=1
	if count>1:
		return False
	else:
		return "".join(combined)



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
						if element1 not in used_terms:
							used_terms.append(element1)
						if element2 not in used_terms:
							used_terms.append(element2)

			if flag==0:
				if element1 not in used_terms:
					prime_implicants.append(element1)

	for i in terms[number]:
		if i not in used_terms:
			prime_implicants.append(i)

	if not recursion:
		return
	else:
		getPrimeImplicants(new_terms,number-1,prime_implicants)


def main():
	variables,min_terms_categorised = inputData()
	prime_implicants=[]
	getPrimeImplicants(min_terms_categorised,variables,prime_implicants)	
	print (variables,min_terms_categorised)
	print (prime_implicants)

if __name__=="__main__":
	main() 