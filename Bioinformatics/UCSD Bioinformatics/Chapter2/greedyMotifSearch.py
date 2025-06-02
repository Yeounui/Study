def greedyMotifSearch(dna, k, t):
    dnaList = dna.split(" ")
    bestMotifs = [[0]*k, [0]*k, [0]*k, [0]*k]
    for i in range(k):
        for j in range(t):
            base = dnaList[j][i]
            if base == 'A':
                bestMotifs[0][i] += 1
            elif base == 'C':
                bestMotifs[1][i] += 1
            elif base == 'G':
                bestMotifs[2][i] += 1
            elif base == 'T':
                bestMotifs[3][i] += 1
            else:
                return 1

    for i in range(len(dnaList[0])-k + 1):
        motifList = []
        for j in range(k):
            bestProp = bestMotifs[0][j]
            motifBase = 0
            for k in range(1, 4):
                candidProp = bestMotifs[k][j]
                if bestProp < candidProp:
                    bestProp = candidProp
                    motifBase = k
            motifList.append(motifBase)
            motifBase = 0
        each k-mer Motif in the first string from Dna
        Motif1 ← Motif
        for i = 2 to t
            form Profile from motifs Motif1, …, Motifi - 1
            Motifi ← Profile-most probable k-mer in the i-th string in Dna
        Motifs ← (Motif1, …, Motift)
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
    return BestMotifs