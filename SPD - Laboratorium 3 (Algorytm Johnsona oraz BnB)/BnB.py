from Natural_permutation import Natural_permutation
import copy

class Branch_and_Bound (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = n - 1


    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + "\n" + str1 + str(self.UB)

    def BranchAndBound(self):
        Pi = []
        for i in range(0, len(self.P_Copy)):
            self.BnB(i,copy.deepcopy(self.P_Copy), copy.deepcopy(Pi), copy.deepcopy(self.Nr))

    def BnB(self, j_star, P, Pi, Nr):
        Pi.append(Nr[j_star])
        del P[j_star]
        del Nr[j_star]
        if len(P) > 0:
            LB = self.LowerBound(copy.deepcopy(Pi),copy.deepcopy(P))
            if LB < self.UB:
                for j in range(0, len(P)):
                    self.BnB(j, copy.deepcopy(P), copy.deepcopy(Pi), copy.deepcopy(Nr))
        else:
            Cmax = self.CalculateCustomCmax(Pi)
            if Cmax < self.UB:
                self.UB = Cmax
                self.Pi = Pi
                self.CalculateCmax()
                self.CalculateSmax()
            print(self.Pi)

    def LowerBound(self, Pi, P):
        Clb = self.CalculateCustomC(Pi)
        Plb = 0
        LBmax = 0
        for i in range (0, self.m):
            for j in range(0, len(P)):
                Plb = Plb + P[j][i]
                
            Pminimum=0
            for k in range(i+1, self.m):
                Pmin = P[0][k]
                for a in range(1, len(P)):
                    if P[a][k] < Pmin:
                        Pmin = P[a][k]
                Pminimum = Pminimum + Pmin
            if LBmax < Clb[len(Pi)-1][i] + Plb + Pminimum:
                LBmax = Clb[len(Pi)-1][i] + Plb + Pminimum
            Plb = 0
        return LBmax

    def CalculateCustomC(self, Pi):
        C = []
        for i in range(0, len(Pi)):
            z = [None] * self.m
            C.append(z)

        C[0][0] = self.P[Pi[0] - 1][0]

        for i  in range(1, self.m):
            C[0][i] = C[0][i-1] + self.P[Pi[0] - 1][i]
            
        for i in range(1,len(Pi)):
            C[i][0] = C[i-1][0] + self.P[Pi[i] - 1][0]

        for a in range(1,self.m):
            for i in range(1,len(Pi)):
                C[i][a] = max(C[i-1][a],C[i][a-1]) + self.P[Pi[i] - 1][a]
        return C
