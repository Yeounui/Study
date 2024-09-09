def DNAcompression(seq):
    """
    >>> DNAcompression('ACCC-GTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    'ACCC-A-G-ET-ZA-DA'
    """
    encoded = ''
    basePos = 0
    repeat = 0
    while basePos < len(seq):
        currentBase = seq[basePos]
        if currentBase == '-':
            encoded += '-A-'
            basePos += 1
        else:
            while basePos < len(seq):
                if currentBase == seq[basePos]:
                    repeat += 1
                    basePos += 1
                    if repeat == 26:
                        encoded += ('-Z' + currentBase)
                        repeat = 0
                else:
                    if repeat >= 4:
                        encoded += ('-' + str(chr(64 + repeat)) + currentBase)
                    else:
                        encoded += "".join((currentBase,) * repeat)
                    repeat = 0
                    break

    if repeat >= 4:
        encoded += ('-' + str(chr(64 + repeat)) + currentBase)
    else:
        encoded += "".join((currentBase,) * repeat)

    return encoded

def DNAdecompression(encoded):
    """
    >>> DNAdecompression('ACCC-A-G-ET-ZA-DA')
    'ACCC-GTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    """
    seq = ''
    digitPose = 0
    while digitPose < len(encoded):
        if encoded[digitPose] == '-':
            seq += "".join((encoded[digitPose+2],)*(ord(encoded[digitPose+1])-64))
            digitPose += 3
        else:
            seq += encoded[digitPose]
            digitPose += 1
    return seq