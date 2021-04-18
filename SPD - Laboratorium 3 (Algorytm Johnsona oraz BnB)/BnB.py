from Natural_permutation import Natural_permutation

class Branch_and_Bound (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = len(self.P) - 1

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 

    def BranchAndBound(self):
        #UB=initUB?
        Pi = []
        for i in self.P_copy:
            BnB(i,self.P_copy, Pi)

    def BnB(self, P, j_star, Pi):
        Pi.append(j_star)
        del P[j_star]
        if len(P) > 0:
            #LB<-Bound(Pi,N)?
            if LB < UB:
                for j in P:
                    BnB(j,P,Pi)
        else:
            #Cmax <- calculate Pi
            if Cmax < UB:
                UB = Cmax
                self.Pi = Pi