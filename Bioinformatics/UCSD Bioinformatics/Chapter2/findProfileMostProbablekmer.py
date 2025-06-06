def findProfileMostProbablekmer(text, k, matrix):
    matRowList = matrix.split('\n')
    matDict = {'A': [float(c0) for c0 in matRowList[0].split(' ')],
               'C': [float(c1) for c1 in matRowList[1].split(' ')],
               'G': [float(c2) for c2 in matRowList[2].split(' ')],
               'T': [float(c3) for c3 in matRowList[3].split(' ')]}
    
    bestScore = 0
    bestLocus = -1
    for i in range(len(text)-k+1):
        candidate = text[i:i+k]
        score = 0
        for j, c in enumerate(list(candidate)):
            score += matDict[c][j]
        if score > bestScore:
            bestLocus = i
            bestScore = score
            
    return text[bestLocus:bestLocus+k]


if __name__ == "__main__":
    text = "AGCATCGAGTCGTATTGAGGGGACAAACCAGCAGATGCGGTAGGCTATTAAGGCCACGTCTCCGACGTGTCCCCTTGGCAGATGGAGTTGGCCCCGCGCCATATGGGCGCATTGGTGGCAGTGTACTAAAGAAAACCGGGATAGCTTAACTAACCAATGATCCGCTAGAAATTGTACGGGGTGTCCATGTTAACTGCTTCCGTCGGCCTATTGGGTTATCCAGTGGTCGATCCCCAGCTGACTATTGGGATTCCTCGCGCTAACGTAGAGAAAATCATGACGCCTTACGCGCGGCAGACGACTCTACGCCCCGGCTCTGGAATACTGTACCCCCTCGTCCTTCCCTCGTTAGTTTATTAGACTTGTACATCACGAGAGTTTTGGACTCCCACCGCCTCGAATACATAGGAATAACCACGCTGGAGGGTATCAGTCTAGTAACCACAATAATCACGAAATACTTGAGACGCGCCATGGGGTATTGGATCCTCGACGAGCGATGTCATTCTGCATGGGCGCGAAAAACACTCGCCTGACTCGAAGTGCTGACGGCTTACCCACGCTGCGGCTTGGCGTCCTGACTCGTCTTCTTACGCGGGGCCACGTCCTGCAGCAATCTGACCGGAGAATGTCACATACGCCCAAGCGAGGCAGATATGTGACTGTACGTACACAACAAGATGAGTGTTATACACAACGCGGTATAAGAGACTGTTACTCTGACTTCTGCAATGCAGCTTGCCAGTGATAGTCCGACTTCGACCACGTTACGGGTCTACCAGTAGCGACCGAGAACATGGATTGCACCTATGAGTTACTATGCGCCTTTTCACGTCGCGGCCAGTAAGTAATGGCTCTCGGTAAAAAAAATCTCGTTAACAGGCGCAACCTGATGGGAGTCTTGCGTCAGGAGTTAGAACCAACTTATGTGGTTGACAGGGAACCATCCATCACGGCTGTTCGTCTTGCCAAGGGACGATGGGAGGTCTTTAAATAAGTG"
    k = 12
    matrix = "0.217 0.253 0.265 0.241 0.289 0.325 0.181 0.277 0.217 0.181 0.241 0.289\n0.313 0.253 0.301 0.169 0.217 0.229 0.277 0.217 0.313 0.361 0.229 0.277\n0.217 0.301 0.265 0.325 0.253 0.205 0.265 0.301 0.241 0.205 0.265 0.193\n0.253 0.193 0.169 0.265 0.241 0.241 0.277 0.205 0.229 0.253 0.265 0.241"
    print(findProfileMostProbablekmer(text, k, matrix))