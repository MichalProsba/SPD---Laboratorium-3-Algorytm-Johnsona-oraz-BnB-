from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Johnson_algorithm import Johnsone_algorithm
   
#natural_permutation = Natural_permutation(1,6,2)
#print(natural_permutation)
str1 = "===================================================================\n"
johnson = Johnsone_algorithm(1,6,2)
print (str1 + "BEFORE JOHNSON ALGORITHM")
print(johnson)
johnson.Johnson()
print (str1 + "AFTER JOHNSON ALGORITHM")
print(johnson)