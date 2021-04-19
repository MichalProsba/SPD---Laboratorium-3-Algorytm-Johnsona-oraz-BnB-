from Johnson_algorithm import Johnsone_algorithm
from Johnson_algorithm import Johnsone_algorithm
import copy

class Johnsone_algorithm3 (Johnsone_algorithm) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

    #    self.P_virtual = []

    #    for a in range(0, n):
    #        a = [None] * (m-1)
    #        self.P_virtual.append(a)

    #    #for j in range(0,n):
    #    #    self.P_virtual[j][0] = self.P_Copy[j][0]

    #    #for j in range(0,n):
    #    #    self.P_virtual[j][1] = self.P_Copy[j][2]

    #    for i in range(0, m-1):
    #        for j in range(0,n):
    #            self.P_virtual[j][i] = self.P_Copy[j][i] + self.P_Copy[j][i+1]

    #    self.P_copy = self.P_virtual
    #    self.m = 3
    #    #self.johnson2 = Johnsone_algorithm(1, self.n, self.m-1)
    #    #self.johnson2.P = copy.deepcopy(self.P_virtual)
    #    #self.johnson2.P_copy = copy.deepcopy(self.P_virtual)
    #    #self.johnson2.Johnson()
    #    #self.Pi = self.johnson2.Pi
    #    #print("x")


    #def __str__(self):
    #    str1 = "===================================================================\n"
    #    return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)