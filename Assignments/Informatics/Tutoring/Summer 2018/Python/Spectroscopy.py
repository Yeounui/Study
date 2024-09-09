def referenceSpectra(textfile):
    opentxt = open(textfile, 'r')
    readtxt = opentxt.readline()
    spectradict = dict()
    while readtxt:
        interval = readtxt.find('\t')
        predictvalue = sorted(list(map(float, readtxt[interval+1:].strip().split(','))))
        spectradict[readtxt[:interval]] = tuple(predictvalue)
        readtxt = opentxt.readline()
    opentxt.close()
    return spectradict

def referenceLines(spectrum, referencespectrum, eps = 0.1):
    wavelengthnumber = 0
    for referredwavelength in referencespectrum:
        switch = 0
        for measuredwavelength in spectrum:
            if abs(measuredwavelength - referredwavelength) <= eps:
                switch = 1
                break
        if switch == 1:
            wavelengthnumber += 1
    return wavelengthnumber

def decomposition(spectra, referencespectra, eps = 0.1, minimum = None):
    elementlist = list()
    for element in referencespectra:
        foundnumber = referenceLines(spectra, referencespectra[element], eps)
        if minimum is None:
            if foundnumber == len(referencespectra[element]):
                elementlist.append(element)
        else:
            if foundnumber >= minimum:
                elementlist.append(element)
    return sorted(elementlist)
        

referenceSpectrum = referenceSpectra('spectra.txt')
print(referenceSpectrum['H'])
print(referenceSpectrum['Li'])
spectrum1 = (410.1055, 434.1126, 434.1427, 486.3071, 656.224)
print(referenceLines(spectrum1, referenceSpectrum['H']))
spectrum2 = (410.1875, 434.0906, 486.2315, 524.7571, 656.2779)
print(referenceLines(spectrum2, referenceSpectrum['H'], eps=0.1))
print(referenceLines(spectrum2, referenceSpectrum['H'], eps=0.025))
spectrum = (402.5579, 410.1914, 413.162, 434.1243, 486.0598, 504.7387, 610.157, 610.562, 656.354, 670.578, 670.991)
print(decomposition(spectrum, referenceSpectrum))
print(decomposition(spectrum, referenceSpectrum, eps=0.2))
print(decomposition(spectrum, referenceSpectrum, minimum=2))
print(decomposition(spectrum, referenceSpectrum, eps=0.2, minimum=2))