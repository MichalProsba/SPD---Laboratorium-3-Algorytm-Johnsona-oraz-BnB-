from Natural_permutation import Natural_permutation

class Branch_and_Bound (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = len(self.P) - 1
        #Inicjalizacja UB
        self.UB = self.C[n-1][m-1]

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 

    def BranchAndBound(self):
        Pi = []
        for i in range(0, len(self.P_Copy)):
            BnB(i,self.P_copy, Pi)

    def BnB(self, j_star, P, Pi):
        Pi.append(self.Nr_Copy[j_star])
        del P[j_star]
        del self.Nr_Copy[j_star]
        if len(P) > 0:
            #LB = Bound(Pi,P)? napisać funkcję do wyznaczania LB
            if LB < self.UB:
                for j in range(0, len(P)):
                    BnB(j,P,Pi)
        else:
            Cmax = self.CalculateCustomCmax(Pi)
            if Cmax < self.UB:
                self.UB = Cmax
                self.Pi = Pi

    def Bound(self, Pi, P):
        x=0