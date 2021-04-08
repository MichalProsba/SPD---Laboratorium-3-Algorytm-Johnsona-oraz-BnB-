from Generator import RandomNumberGenerator

class Natural_Permutation:
    def __init__(self, seed, n, m):
        rng = RandomNumberGenerator(seed)
        #Numer 
        #Numer zadania
        self.Nr = []
        #Czas wykonania
        self.P = []
        for i in range(0, n):
            #Numer zadania
            nr = []
            #Czas wykonania
            p = []
            #Losujemy liczby z przedzialu od 1 do 29 calkowite
            #Numerujemy zadania
            for j in range(0, m):
                p.append(rng.nextInt(1,29))
            self.P.append(p)
            
            

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + str(self.Nr) + "\n" + str(self.P) + "\n" + str1

   
natural_permutation = Natural_Permutation(1,6,2)
print(natural_permutation)

