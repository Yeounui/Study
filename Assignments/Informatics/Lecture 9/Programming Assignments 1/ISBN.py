'''
Created on 2016. 11. 14.

@author: korea
'''
def overview(codes):
    Errors = list()
    Counts = {'English speaking countries': 0, 'French speaking countries': 0, 'German speaking countries': 0, 'Japan': 0, 'Russian speaking countries': 0, 'China': 0, 'Other countries': 0, 'Errors': 0}
    result = ''
    for code in codes:
        if code[0:3] == '978' or code[0:3] == '979':
            oddnum = 0
            evenum = 0
            for digit in code[0: 12: 2]:
                oddnum += int(digit)
            for digit in code[1: 12: 2]:
                evenum += int(digit)
            calculated = (10-(oddnum + 3*evenum)%10)%10
            given = int(code[-1])
            if given == calculated:
                if code[3] == '0' or code[3] == '1':
                    Counts['English speaking countries'] += 1
                elif code[3] == '2':
                    Counts['French speaking countries'] += 1
                elif code[3] == '3':
                    Counts['German speaking countries'] += 1
                elif code[3] == '4':
                    Counts['Japan'] += 1
                elif code[3] == '5':
                    Counts['Russian speaking countries'] += 1
                elif code[3] == '7':
                    Counts['China'] += 1
                else:
                    Counts['Other countries'] += 1
            else:
                Counts['Errors'] += 1
            
        else:
            Counts['Errors'] += 1
    
    print('English speaking countries: ' + str(Counts['English speaking countries']) + '\n' +
          'French speaking countries: ' + str(Counts['French speaking countries']) + '\n' +
          'German speaking countries: ' + str(Counts['German speaking countries']) + '\n' +
          'Japan: ' + str(Counts['Japan']) + '\n' +
          'Russian speaking countries: ' + str(Counts['Russian speaking countries']) + '\n' +
          'China: ' + str(Counts['China']) + '\n' +
          'Other countries: ' + str(Counts['Other countries']) + '\n' +
          'Errors: ' + str(Counts['Errors']))
    
codes = ['9780625599844', '9797115373716', '9792979955337', '9797336257642','9789593306607', '9789694325293', '9791822296504', '4290382535184','9785350231540', '9783278251220', '9798523783890', '9794912755004','4053033536332', '9791752533403', '9792606726606', '9792395739535','9784555397624', '9780447107678', '9792369140459', '9799576687999','9787523361849', '9797050391516', '9788736912064', '9780827124813','9799531212193', '9783404796991', '9794649223043', '9782476068722','9794678781804', '9780158274461', '9796849025502', '7460643135195','9783166909875', '9788744245437', '9780162652255', '9787132044477','9799817715948', '9792371721905', '9794656384843', '9799183123255','9797531625758', '9786242658858', '9799880439390', '9793329399399','9792863952640', '9793661514177', '9781494452230', '9784241745357','9784485394731', '9787198987917', '9782504526392', '9784227439836']
overview(codes)