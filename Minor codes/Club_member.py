'''
Created on 2018. 3. 18.

@author: Seungchan Oh
This is for selecting members among candidates.
'''
applicants = [('L.CY', 0), ('S.SY', 1), ('B.SM', 1), ('JW', 1), ('L.HS', 0), ('SE',0)]

import random
Lotterybox = list()

for order_of_arrival, applicant in enumerate(applicants):
    if applicant[1] == 0:
        Lotterybox.append(applicant[0])
    if order_of_arrival in range(0,2):
        Lotterybox.append(applicant[0])
    Lotterybox.append(applicant[0])

print(random.sample(Lotterybox, 2))