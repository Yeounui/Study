'''
Created on 2016. 10. 3.

@author: korea
'''
givenstr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?!.-()<>%$',:_/\""
transstr="ɐqɔpǝɟƃɥᴉɾʞ˥ɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀΌɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86 ¿¡˙-)(><%$,':‾\/"
numstr = int(input())
rvqueue = ''
rvqueln = ''
rvquecl = ''

for line in range(0, numstr):
    queue = input()
    for letter in queue:
        indlet = givenstr.find(letter)
        rvqueue += transstr[indlet]
    rvqueln += str(len(rvqueue))
    rvquecl += rvqueue
    rvqueue = ''

rvquecl=rvquecl[::-1]

for prsepar in range(1, numstr+1):
    separ=numstr-prsepar
    cutline = rvqueln[2*separ:]
    rvqueln=rvqueln[:2*separ]
    cutline = int(cutline)
    rvrvline = rvquecl[0:cutline]
    rvquecl = rvquecl[cutline:]
    print(rvrvline)
    
    
    