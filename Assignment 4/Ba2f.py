def Score(MotifList): #Attempt to find the Score (which is the Hamming Distance?), unfortunately unfinished
    Adenin_Count = 0
    Cytosin_Count = 0
    Guanin_Count = 0
    Thymin_Count = 0
    
    for a in MotifList:
        for b in a:
            if b == "A":
                Adenin_Count += 1
            if b == "C":
                Cytosin_Count += 1
            if b == "G":
                Guanin_Count += 1
            if b == "T":
                Thymin_Count += 1


        
        

def randomizedsearch(Dna, k):
    t = len(Dna)
    MotifList = []
    from random import randint
    a = randint(0, len(Dna[0])-k)
    for i in Dna:
        MotifList += [i[a:a+k]] #adds the random k-mer (motif) from string i as an array to the initially empty Motif-List MotifList. Im relatively sure this should already be the Profile, Im just corrently failing to find the Score
    BestMotifs = MotifList
    while True:
        Profile = FindProfile(MotifList)
        Motifs = MotifList(Profile, Dna)
        if Score(MotifList) < Score(BestMotifs):
            BestMotifs = MotifList
        else:
            return BestMotifs        

#randomizedsearch(["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"], 8)

