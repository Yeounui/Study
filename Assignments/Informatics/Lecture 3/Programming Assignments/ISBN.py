'''
Created on 2016. 9. 14.

@author: korea
'''
x1=int(input())
x2=int(input())
x3=int(input())
x4=int(input())
x5=int(input())
x6=int(input())
x7=int(input())
x8=int(input())
x9=int(input())
x10=int(input())

D = (x10 == (1*x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9) % 11)

if D : #D 혼자 쓰면 이게 true일 경우라는 뜻
    print('OK')
else :
    print('WRONG')