from Generator import RandomNumberGenerator
import copy

class Natural_permutation:
    def __init__(self, seed, n, m):
        rng = RandomNumberGenerator(seed)        
        #Liczba zadan
        self.n = n
        #Liczba maszyn
        self.m = m
        #Permutacja po uszeregowaniu
        self.Pi = []
        # Macierz czas wykonania
        self.P = []
        # Lista zadań do wykonania
        self.Nr = []
        # Macierz czasów wykonania
        self.P_Copy = []
        # Lista zadań do wykonania
        self.Nr_Copy = []
        # Macierz czasów zakończenia zadań
        self.C = []
        # Macierz czasów trwania zadań
        self.S = []

        for i in range(1, n+1):
            self.Pi.append(i)

        for i in range(0, n):
            z = [None] * m
            self.C.append(z)

        for i in range(0, n):
            x = [None] * m
            self.S.append(x)

        for i in range(0, n):
            #Czas wykonania
            p = []
            #Losujemy liczby z przedzialu od 1 do 29 calkowite
            #Numerujemy zadania
            for j in range(0, m):
                p.append(rng.nextInt(1,29))
            self.P.append(p)
            self.P_Copy.append(p)

        for i in range(1, n+1):
            self.Nr.append(i)
            self.Nr_Copy.append(i)

        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[n-1][m-1])
        
    def CalculateCmax(self):
        self.C[0][0] = self.P[self.Pi[0] - 1][0]

        for i in range(1, self.m):
            self.C[0][i] = self.C[0][i-1] + self.P[self.Pi[0] - 1][i] 
        
        for i in range(1,self.n):
            self.C[i][0] = self.C[i-1][0] + self.P[self.Pi[i] - 1][0]

        for a in range(1,self.m):
            for i in range(1,self.n):
                self.C[i][a] = max(self.C[i-1][a],self.C[i][a-1]) + self.P[self.Pi[i] - 1][a]

    def CalculateCustomCmax(self, Pi):
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
        return C[len(Pi)-1][self.m-1]

    def CalculateSmax(self):
        for i in range(0,self.n):
            for j in range(0,self.m):
                self.S[i][j] = self.C[i][j] - self.P[self.Pi[i] - 1][j]

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)
