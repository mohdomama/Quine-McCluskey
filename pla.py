import tabulation

def combination(functions,index, selections, temp):
	if index == len(functions):
		temp1=temp+ []							
		selections.append(temp1)
		return
	else:
		for i in functions[index]:
			temp.append(i)
			combination(functions,index+1, selections, temp)
			temp.remove(i)

def leastAND (selections):
	minimum = len(set([x for y in selections[0] for x in y]))
	leastAND_combination = selections[0]
	for i in selections:
		if minimum > len(set([x for y in i for x in y])):
			minimum = len(set([x for y in i for x in y]))
			leastAND_combination = i

	return leastAND_combination 

def main():
	functions = []
	for i in range(int(input("Enter number of functions:\n"))):
		variables = int(input("Enter the number of variables:\n"))
		all_terms = [x for x in range(0,2**variables)]
		min_terms = [int(x) for x in input("Enter the minterms (space seperated) :\n").split()]
		_, _ ,function1 = tabulation.tabulation(variables, min_terms)

		_, _ ,function2 = tabulation.tabulation(variables, list( set(all_terms)^set(min_terms) ))

		print("\nThe possible functions are:")
		for i in function1 :
			tabulation.printing(i,'+')
		for i in function2 :
			tabulation.printing(i,'+')

		functions.append(function1 + function2)

	selections = []
	combination(functions,0, selections, [])

	print("The combinations are:\n")
	for i in selections:
		print(i)

		print("NEXT")

 
	print("The least and combination that solves all functions are:\n")
	for i in leastAND(selections):
		tabulation.printing(i,'+')
	

	


if __name__ == "__main__":
	main()