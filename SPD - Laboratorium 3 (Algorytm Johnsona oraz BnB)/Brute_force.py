from Natural_permutation import Natural_permutation

class Brute_force (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = len(self.P) - 1

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 