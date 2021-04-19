from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Johnson_algorithm import Johnsone_algorithm
from Johnson_algorithm3 import Johnsone_algorithm3
from Brute_force import Brute_force
from BnB import Branch_and_Bound

seed = 1
tasks = 7
machines = 3

str1 = "===================================================================\n"
print (str1 + "NATURAL PERMUTATION")
natural_permutation = Natural_permutation(seed, tasks, machines)
print(natural_permutation)

johnson3 = Johnsone_algorithm3(seed, tasks, machines)
johnson3.Johnson()
print (str1 + "AFTER JOHNSON ALGORITHM3")
print(johnson3)

#johnson = Johnsone_algorithm(seed, tasks, machines)
#johnson.Johnson()
#print (str1 + "AFTER JOHNSON ALGORITHM")
#print(johnson)

#print (str1 + "BRUTE_FORCE")
#brute_force = Brute_force(seed, tasks, machines)
#brute_force.First_Brute_force()
#print(brute_force)
#print (str1 + "BnB")
#bnb = Branch_and_Bound(seed, tasks, machines)
#bnb.BranchAndBound()
#print(bnb)