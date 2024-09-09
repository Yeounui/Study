'''
Created on 2016. 9. 10.

@author: korea
'''
Nation = input()
EW = float(input()) 
LE = float(input())
EF = float(input())

HPI = (EW * LE) / EF

print('The HPI of '+ Nation + ' is ' + ("{:.2f}.".format(HPI))) # "{:.2f}."는 구조/":"는 '정의를 시작'/".2f"은 '.뒤에 두자리 구조로 소수로 표현하겠다'
