from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Johnson_algorithm import Johnsone_algorithm
from Brute_force import Brute_force

str1 = "===================================================================\n"
print (str1 + "NATURAL PERMUTATION")
natural_permutation = Natural_permutation(1,3,3)
print(natural_permutation)
#johnson = Johnsone_algorithm(1,6,2)
#print (str1 + "BEFORE JOHNSON ALGORITHM")
#print(johnson)
#johnson.Johnson()
#print (str1 + "AFTER JOHNSON ALGORITHM")
#print(johnson)

#print(natural_permutation.CalculateCustomCmax(johnson.Pi))

brute_force = Brute_force(1,3,3)
brute_force.First_Brute_force()
print(brute_force)