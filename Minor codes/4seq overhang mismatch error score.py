import pandas as pd

"""
This script is for finding adequate overhangs to minimize inference
of overhangs for Golden-gate assembly.

Pryor JM, Potapov V, Kucera RB, Bilotti K, Cantor EJ, et al. (2020)
Enabling one-pot Golden Gate assemblies of unprecedented complexity using data-optimized 
assembly design. PLOS ONE 15(9): e0238592. https://doi.org/10.1371/journal.pone.0238592"
"""

readExcel = pd.read_excel('pone.0238592.s001.xlsx')
print(readExcel)

inputOverhangs = ["GGAG", "CTCC", "TGAC", "GTCA", "TCCC", "GGGA",
                  "TACT", "AGTA", "CCAT", "ATGG",
                  "AATG", "CATT", "ACCT", "AGGT", "GAAA", "TTTC",
                  "GCTT", "AAGC", "TGTT", "AACA", "TTCG", "CGAA",
                  "ACAA", "TTGT", "CGCT", "AGCG"]
totalErrorScore = 0
reportError = dict()

def revseq(overhang):
    resultseq = ''
    for digit in overhang[::-1]:
        if digit == 'A':
            resultseq += 'T'
        elif digit == 'T':
            resultseq += 'A'
        elif digit == 'C':
            resultseq += 'G'
        else:
            resultseq += 'C'
    return resultseq

duplicatedOverhangCheck = list()
for overhang1 in inputOverhangs:
    for overhang2 in inputOverhangs:
        if overhang1 != overhang2:
            if overhang1 != revseq(overhang2):
                overhangSet = set([overhang1, overhang2])
                if not overhangSet in duplicatedOverhangCheck:
                    errorScore = readExcel[readExcel["Overhang"]==overhang1].iloc[0][overhang2]
                    print(errorScore)
                    totalErrorScore += errorScore
                    reportError[overhang1 +', '+ overhang2] = errorScore
                    duplicatedOverhangCheck.append(overhangSet)

print(totalErrorScore)
print(reportError)
onlymeaningful = dict()
for key in reportError.keys():
    if reportError[key] != 0:
        onlymeaningful[key] = reportError[key]
print(onlymeaningful)