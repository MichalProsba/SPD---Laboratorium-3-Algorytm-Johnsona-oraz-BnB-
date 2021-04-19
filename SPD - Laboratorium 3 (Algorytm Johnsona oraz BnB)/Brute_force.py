from Natural_permutation import Natural_permutation
import copy

class Brute_force (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = n - 1

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + "\n" + str1 + str(self.UB)

    def First_Brute_force(self):
        Pi = []
        for i in range(0, len(self.P_Copy)):
            self.Brute_force(i,copy.deepcopy(self.P_Copy), copy.deepcopy(Pi), copy.deepcopy(self.Nr))

    def Brute_force(self, j_star, P, Pi, Nr):
        Pi.append(Nr[j_star])
        del P[j_star]
        del Nr[j_star]
        if len(P) > 0:
            for j in range(0, len(P)):
                self.Brute_force(j, copy.deepcopy(P), copy.deepcopy(Pi), copy.deepcopy(Nr))
        else:
            Cmax = self.CalculateCustomCmax(Pi)
            if Cmax < self.UB:
                self.UB = Cmax
                self.Pi = Pi
                self.CalculateCmax()
                self.CalculateSmax()
            #print(self.Pi)