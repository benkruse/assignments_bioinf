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

def FindConsensus(Dna):#Finds the Consensus sequence over all equally long DNA-Strings in Dna.
    ConsensusString = ""
    for a in range (0,len(Dna[0])):
        Adenin_Count = 0
        Cytosin_Count = 0
        Guanin_Count = 0
        Thymin_Count = 0
        for b in Dna:
            if b[a] == "A":
                Adenin_Count += 1
            if b[a] == "C":
                Cytosin_Count += 1
            if b[a] == "G":
                Guanin_Count += 1
            if b[a] == "T":
                Thymin_Count += 1
        helplist = [Adenin_Count, Cytosin_Count, Guanin_Count, Thymin_Count]
        MostFrequentMotif = max(helplist) #due to the nature of Pythons max-function, the first most frequent nucleotide will be chosen for the consensus sequence (in a tie, Adenine will be chose over the rest, Cytosine over Guanine and Thymine and Guanine over Thymine).
        if MostFrequentMotif == Adenin_Count:
            ConsensusString += "A"
            continue
        if MostFrequentMotif == Cytosin_Count:
            ConsensusString += "C"
            continue
        if MostFrequentMotif == Guanin_Count:
            ConsensusString += "G"
            continue
        if MostFrequentMotif == Thymin_Count:
            ConsensusString += "T"
    return ConsensusString
        
def GibbsSampling(Dna, k):
    t = len(Dna)
    MotifList = []
    from random import randint
    for i in Dna:
        a = randint(0, len(Dna[0])-k)
        MotifList += [i[a:a+k]] #adds the random k-mer (motif) from string i as an array to the initially empty Motif-List MotifList.
    Current_Score = DistanceBetweenPatternAndStrings(FindConsensus(MotifList), MotifList)
    while True:
        ShortenedDna = Dna
        NumberOfRemovedString = randint(0, t-1)
        RemovedStrand = ShortenedDna.pop(NumberOfRemovedString)
        Profile = MakeProfile(ShortenedDna, len(Dna[0]))
        MotifProbabilityList = []
        MotifListOfRemovedStrand = []
        for a in range (0, len(RemovedStrand)-k):
            MotifListOfRemovedStrand += [RemovedStrand[a:a+k]]
            MotifProbabilityList += [MotifProb(RemovedStrand[a:a+k], Profile, k)]
        Circle_Counter = 0
        SmallestProbability = min(MotifProbabilityList)
        for Probability in MotifProbabilityList:
            MotifProbabilityList[Circle_Counter] = MotifProbabilityList[Circle_Counter]/SmallestProbability
            Circle_Counter += 1
        MotifProbabilityListSum = sum(MotifProbabilityList)
        Circle_Counter = 0
        for Probability in MotifProbabilityList:
            MotifProbabilityList[Circle_Counter] = MotifProbabilityList[Circle_Counter]/MotifProbabilityListSum
            Circle_Counter += 1
        NextMotifNumber = ChooseNextMotifNumber(MotifProbabilityList)
        MotifList[NumberOfRemovedString] = MotifListOfRemovedStrand[NextMotifNumber]
        New_Score = DistanceBetweenPatternAndStrings(FindConsensus(MotifList), MotifList)
        if New_Score <= Current_Score:
            return MotifList
        else:
            Current_Score = New_Score
        
            

def MotifProb(Motif, Profile, k): #calculates the probability for k-mer Motif according to the probability profile.
    Probability = 1
    for a in range(0,k):
        if Motif[a] == "A":
            Probability = Probability * Profile[0][a]
        if Motif[a] == "C":
            Probability = Probability * Profile[1][a]
        if Motif[a] == "G":
            Probability = Probability * Profile[2][a]
        if Motif[a] == "T":
            Probability = Probability * Profile[3][a]
    return Probability

def MakeProfile(MotifList, l): #creates a probability profile in the form of a 4xl-Matrix, listing the probabilies of Adenine, Cytosine, Guanine and Thymine in that order. l is the shared length of the elements in MotifList.
    t = len(MotifList)
    import numpy
    Profile = numpy.zeros((4,l))
    for a in range (0,l):
        Adenin_Count = 1 #the nucleotide_Counts begin with 1 to take pseudo counts into account.
        Cytosin_Count = 1
        Guanin_Count = 1
        Thymin_Count = 1
        for b in MotifList:
            if b[a] == "A":
                Adenin_Count += 1
            if b[a] == "C":
                Cytosin_Count += 1
            if b[a] == "G":
                Guanin_Count += 1
            if b[a] == "T":
                Thymin_Count += 1
        Profile[0] [a] = Adenin_Count / (t+4) #we add 4 again to take pseudo counts into account.
        Profile[1] [a] = Cytosin_Count / (t+4)
        Profile[2] [a] = Guanin_Count / (t+4)
        Profile[3] [a] = Thymin_Count / (t+4)
    return Profile

def ChooseNextMotifNumber(ProbabilityList): #Chooses the next motif of the removed string of Dna at random but weighted by the probabilities of that motif happening (only returning the index of that motif, not the motif itself).
    Counter = 0
    from random import uniform
    randfloat = uniform (0, 1)
    for a in range(0, len(ProbabilityList)):
        Counter += ProbabilityList[a]
        if Counter >= randfloat:
            return a


#FindConsensus(['GGGTGTTC', 'TGTAAGTG', 'CGAAAGAA', 'CAGGTGCA', 'CCACGTGC'])
#FindConsensus(["ACGGA", "ACGGA", "ATTGC"])
#("ATTC", "GTCA", "ACTG", "GTAA", "TCCA")        
#ChooseNextMotifNumber([0.15, 0.2, 0.53, 0.22])           
#MakeProfile(["GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"], 8)    
#MakeProfile(["ACC", "TCC", "GTT"], 3)
#MotifProb("ATA", MakeProfile(["ACC", "TCC", "GTT"], 3), 3)
#GibbsSampling(["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"], 8)
