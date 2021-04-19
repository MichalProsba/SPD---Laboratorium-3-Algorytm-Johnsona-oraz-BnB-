from Generator import RandomNumberGenerator

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
        
    def CalculateCmax(self):
        self.C[0][0] = self.P[self.Pi[0] - 1][0]
        self.C[0][1] = self.C[0][0] + self.P[self.Pi[0] - 1][1] 
        for i in range(1,self.n):
            self.C[i][0] = self.C[i-1][0] + self.P[self.Pi[i] - 1][0]
        for i in range(1,self.n):
            self.C[i][1] = max(self.C[i-1][1],self.C[i][0]) + self.P[self.Pi[i] - 1][1]

    def CalculateCustomCmax(self, Pi):
        C = []
        for i in range(0, n):
            z = [None] * len(Pi)
            C.append(z)
        C[0][0] = self.P[Pi[0] - 1][0]
        C[0][1] = C[0][0] + self.P[Pi[0] - 1][1] 
        for i in range(1,len(Pi)):
            C[i][0] = C[i-1][0] + self.P[Pi[i] - 1][0]
        for i in range(1,len(Pi)):
            C[i][1] = max(C[i-1][1],C[i][0]) + self.P[Pi[i] - 1][1]
        return C[m-1][len(Pi)-1]

    def CalculateSmax(self):
        for i in range(0,self.n):
            for j in range(0,self.m):
                self.S[i][j] = self.C[i][j] - self.P[self.Pi[i] - 1][j]

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 
