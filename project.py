import pandas as pd

drugs = pd.read_csv("drug.csv")  
prescription = pd.read_csv("PRESCRIPTIONS.csv") 

class NonBinTree:

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def print_node(self):
        return self.val

    def __repr__(self):
        return f"({self.val}): {self.nodes}"


# a = NonBinTree(0)
# a.add_node(1)
# a.add_node(3)
# a.add_node(4)
# a.nodes[2].add_node(2)
# a.nodes[0].print_node()

drug_tree = NonBinTree('otc')
num = -1
total = -1
for drug in drugs['dosage_form']:
    total = total + 1
    flag = 0
    number = -1
    for node in drug_tree.nodes:
        number = number + 1
        if drug == node.print_node():
            flag = 1
            break
    if flag == 0:
        drug_tree.add_node(drug)
        num = num + 1
        drug_tree.nodes[num].add_node(drugs.loc[total]['drug_name'])
        drug_tree.nodes[num].nodes[0].add_node(drugs.loc[total]['ingredient'])
    else:
        drug_tree.nodes[number].add_node(drugs.loc[total]['drug_name'])
        drug_tree.nodes[num].nodes[0].add_node(drugs.loc[total]['ingredient'])

prescription_tree = NonBinTree('prescription')
num = -1
total = -1
for drug in prescription['drug_type']:
    total = total + 1
    flag = 0
    number = -1
    for node in prescription_tree.nodes:
        number = number + 1
        if drug == node.print_node():
            flag = 1
            break
    if flag == 0:
        prescription_tree.add_node(drug)
        num = num + 1
        prescription_tree.nodes[num].add_node(prescription.loc[total]['drug'])
        prescription_tree.nodes[num].nodes[0].add_node(prescription.loc[total]['prod_strength'])
    else:
        prescription_tree.nodes[number].add_node(prescription.loc[total]['drug'])
        prescription_tree.nodes[num].nodes[0].add_node(prescription.loc[total]['prod_strength'])

'''main'''

print('\nWelcome to my little drug search engine!\n')
print('Menu is listed here!\n \
    1. Determine whether a drug is otc or prescription.\n \
    2. Search for the otc medicine.\n \
    3. Search for information of medines with the same dosage form.\n \
    4. Search for the prescription medicine\n \
            ')
            
input1 = input("What do you want to do today? ")

if input1 == '1':
    drug_name = input("\nWhats your medicine you want to identify? ")
    ans = 0
    for type in drug_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 1
                break
    for type in prescription_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 2
                break
    if ans == 1:
        print("\nIt's an otc medcine!")
    elif ans == 2:
        print("\nIt's a prescription medicine!")
    else: 
        print("\nCan't identify.")

    print("\nThank you! Goodbye!\n")  
    exit(0)
elif input1 == '2':
    drug_name = input("\nWhats your medicine you want to search? ")
    ans = 0
    for type in drug_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 1
                print("\ndrug name: " + drug_name)
                print("\ningredient:", drug.nodes[0].print_node())
                break
    for type in prescription_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 2
                print("\ndrug name: " + drug_name)
                print("\ningredient:", drug.nodes[0].print_node())
                break
    if ans == 1:
        print("\nIt's an otc medcine!")
    elif ans == 2:
        print("\nIt's a prescription medicine!")
    else: 
        print("\nCan't identify.")

    print("\nThank you! Goodbye!\n")  
    exit(0)

elif input1 == '3':
    dosage_name = input("\nWhats your dosage form you want to search? ")
    ans = 0
    answer = 0
    for type in drug_tree.nodes:
        if dosage_name == type.print_node():
            answer = 1
            for drug in type.nodes:
                ans = ans + 1
    if answer == 1:
        print("\ndogase form name: " + dosage_name)
        print("\nThere are ", ans, " durgs in this dosage form.")
    if answer == 0:
        print("No such dosage form.")

    print("\nThank you! Goodbye!\n")  
    exit(0)

elif input1 == '4':
    drug_name = input("\nWhats your medicine you want to search? ")
    ans = 0
    for type in drug_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 1
                print("\ndrug name: " + drug_name)
                print("\ningredient:", drug.nodes[0].print_node())
                break
    for type in prescription_tree.nodes:
        for drug in type.nodes:
            if drug_name == drug.print_node():
                ans = 2
                print("\ndrug name: " + drug_name)
                print("\ningredient:", drug.nodes[0].print_node())
                break
    if ans == 1:
        print("\nIt's an otc medcine!")
    elif ans == 2:
        print("\nIt's a prescription medicine!")
    else: 
        print("\nCan't identify.")

    print("\nThank you! Goodbye!\n")  
    exit(0)
else:
    print("\nStop Joking!\n")
    exit(0)
