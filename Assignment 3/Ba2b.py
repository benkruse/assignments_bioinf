def HammingDistance (S, T): #Returns the Hamming Distance between the DNA string S and the longer or equally long DNA string T
    k = len(S) #length of the shorter string
    HammingDistanceList = [] #safes the Hamming Distances between String S and the separate k-mers in T  
    HelpCount = 0 #secures we stay in frame and jump from k-mer to k-mer
    for i in range (k, len(T)+1):
        HammingDistanceCounter = 0 #counts the mismatches in a single string of HammingDistanceList
        for j in range (0, k):
            if T[HelpCount+j]!=S[j]:
                HammingDistanceCounter += 1
        HammingDistanceList += [HammingDistanceCounter]
        HelpCount += 1
    return min(HammingDistanceList)

def DistanceBetweenPatternAndStrings(S, Dna): #Returns the added Hamming Distances between one String S and a list Dna containing every DNA-String T_n comprised of n longer (or equally long, theoretically) nucleotides.
    distance = 0
    for T in Dna: 
        distance += HammingDistance(S, T)
    return distance

def NumberToPattern (index, k): #turns a number in quaternary code into its correspondent k-mer
   if k == 1:
      return NumberToSymbol(index)
   PrefixIndex = index // 4
   r = index % 4
   symbol = NumberToSymbol(r)
   PrefixPattern = NumberToPattern(PrefixIndex, k-1)
   return PrefixPattern + symbol

def NumberToSymbol (s): #turns a single number in quaternary code into its correspondent DNA base
   if s == 0:
      return "A"
   if s == 1:
      return "C"
   if s == 2:
      return "G"
   if s == 3:
      return "T"

def MedianString(Dna,k): #returns exactly one of the k-mers which is found most frequently over all DNA-Strings T_n in list Dna
    distance = float("inf")
    for i in range (0, 4**k -1):
        S = NumberToPattern(i, k)
        CurrentHammingDistance = DistanceBetweenPatternAndStrings(S, Dna)
        if distance > CurrentHammingDistance:
            distance = CurrentHammingDistance
            Median = S
    return Median
            

        
#MedianString(["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"], 3)
#MedianString(["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT", "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA", "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT", "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA", "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG", "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA", "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC", "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA", "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG", "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"], 6)
